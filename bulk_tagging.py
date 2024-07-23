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
non_tagged_objects_file = './non_tagged_objects.txt'
tagged_objects_file = './tagged_objects.txt'

def convert_to_second(hh_mm_ss_format):
    hour, minute, second = hh_mm_ss_format.split(':')
    return int(hour) * 3600 + int(minute) * 60 + float(second)

def get_objects_list(lib_id):
    command = ['node', 'LibraryListObjects.js', '\\', '--libraryId', lib_id, '\\', '--fields', '/public/asset_metadata/movie_clips_id', '/public/asset_metadata/info/run_time']
    result = subprocess.run(command, capture_output=True, text=True, cwd=utilities_path, check=True)
    split_lines = result.stdout.strip().split('\n')
    objects = dict()

    for i in range(len(split_lines)):
        if len(split_lines[i]) >= 8 and split_lines[i][:8] == 'objectId':
            j = i + 1
            while j < len(split_lines) and split_lines[j] != '' and split_lines[j] != 'Done.':
                split_spaces = split_lines[j].split(' ')
                info = []
                for part in split_spaces:
                    if part != '':
                        info.append(part)
                try:
                    objects[info[0]] = {"movie_clips_id": info[1], "duration": convert_to_second(info[2])}
                except:
                    print('Object', info[0], 'has wrong metadata format')
                j += 1
            break

    return objects
            

def get_clip_data(object_id, list_objects):
    if list_objects[object_id]["movie_clips_id"] not in movieCLIP_data:
        return

    clip_data = dict()
    clip_data[object_id] = dict()
    clip_data[object_id]["label"] = "Event - ALL"
    clip_data[object_id]["tags"] = list()

    for shot in movieCLIP_data[list_objects[object_id]["movie_clips_id"]].values():
        for label in shot["labels"]:
            if shot["start_time"] < list_objects[object_id]["duration"]:
                clip_data[object_id]["tags"].append({"start_time": int(shot["start_time"] * 1000),
                                                "end_time": int(shot["end_time"] * 1000),
                                                "text": f'{label} ({round(shot["labels"][label], 4)})'})
            
    if len(clip_data[object_id]["tags"]) > 0:
        return clip_data
    

def read_file_txt(file_txt):
    lines = set()
    if os.path.exists(file_txt):
        file = open(file_txt, 'r')
        line = file.readline()
        while line != '':
            lines.add(line.strip())
            line = file.readline()
    return lines

def bulk_tag(lib_id):
    list_objects = get_objects_list(lib_id)
    non_tagged_objects = read_file_txt(non_tagged_objects_file)
    tagged_objects = read_file_txt(tagged_objects_file)
    non_tagged_file = open(non_tagged_objects_file, 'a')
    tagged_file = open(tagged_objects_file, 'a')
    
    for object_id in list_objects:
        if object_id in non_tagged_objects or object_id in tagged_objects:
            continue

        clip_data = get_clip_data(object_id, list_objects)
        if not clip_data:
            non_tagged_file.write(object_id + '\n')
            continue

        write_data(clip_data, clip_json_file)
        command = ['node', 'MezSetVideoTags.js', '\\', '--objectId', object_id, '\\', '--tags', clip_json_file, '\\', '--replace']
        subprocess.run(command, cwd=utilities_path, check=True)
        tagged_file.write(object_id + '\n')

# open(non_tagged_objects_file, 'w').close()
# open(tagged_objects_file, 'w').close()
if __name__ == '__main__':
    bulk_tag(mez_lib_id)
