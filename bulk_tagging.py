import subprocess
import os
import json

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def write_data(data, json_file):
    json_object = json.dumps(data, indent=4)
    with open(json_file, 'w') as file: file.write(json_object)

config_json_file = './config.json'
config_data = read_json_file(config_json_file)

os.environ['FABRIC_CONFIG_URL'] = config_data["config_url"]
os.environ['PRIVATE_KEY'] = config_data["private_key"]
mez_lib_id = config_data["mez_lib_id"]
movieCLIP_json_file = config_data["movieCLIP_json_path"]
clip_json_file = config_data["clip_json_path"]
utilities_path = config_data["utilities_path"]

movieCLIP_data = read_json_file(movieCLIP_json_file)

def get_objects_list(lib_id):
    command = ['node', 'LibraryListObjects.js', '\\', '--libraryId', lib_id, '\\', '--fields', '/public/asset_metadata/movieClips ID']
    result = subprocess.run(command, capture_output=True, text=True, cwd=utilities_path, check=True)
    split_lines = result.stdout.strip().split('\n')
    objects = dict()

    for i in range(len(split_lines)):
        if len(split_lines[i]) >= 8 and split_lines[i][:8] == 'objectId':
            j = i + 1
            while j < len(split_lines) and split_lines[j] != '' and split_lines[j] != 'Done.':
                object_id, clip_id, index = '', '', 0
                while split_lines[j][index] != ' ':
                    object_id += split_lines[j][index]
                    index += 1
                while split_lines[j][index] == ' ':
                    index += 1
                while split_lines[j][index] != ' ':
                    clip_id += split_lines[j][index]
                    index += 1
                objects[object_id] = clip_id
                j += 1
            break

    return objects
        

def get_clip_data(object_id, list_objects):
    clip_data = dict()
    clip_data[object_id] = dict()
    clip_data[object_id]["label"] = "Event - ALL"
    clip_data[object_id]["tags"] = list()

    for shot in movieCLIP_data[list_objects[object_id]].values():
        for label in shot["labels"]:
            clip_data[object_id]["tags"].append({"start_time": int(shot["start_time"] * 1000),
                                            "end_time": int(shot["end_time"] * 1000),
                                            "text": f'{label} ({round(shot["labels"][label], 4)})'})
    return clip_data


def bulk_tag(lib_id):
    list_objects = get_objects_list(lib_id)
    
    for object_id in list_objects:
        clip_data = get_clip_data(object_id, list_objects)
        write_data(clip_data, clip_json_file)
        command = ['node', 'MezSetVideoTags.js', '\\', '--objectId', object_id, '\\', '--tags', clip_json_file, '\\', '--replace']
        subprocess.run(command, cwd=utilities_path, check=True)

bulk_tag(mez_lib_id)
