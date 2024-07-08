# movieCLIP_data_tagging
A bulk tagging script for the ingested MovieCLIP media on the Eluvio Content Fabric.

## MovieCLIP Tags
* Download the complete list of MovieCLIP Tags from this [Drive Link](https://drive.google.com/file/d/15EhA0BT3IF0EuLP1yXr5nn5ad9soxxox/view).
* Each video in MovieCLIP Tags averages 2 minutes in length and typically segmented into 10 to 100 shots tagged with the top 5 labels based on confidence scores.
* More details on MovieCLIP Tags can be found [here](https://github.com/usc-sail/mica-MovieCLIP/blob/main/split_files/README.md).

## Installation

```
git clone https://github.com/eluv-io/elv-utils-js
cd elv-utils-js
git checkout mez-video-tag
npm install
```

## Configuration Setup
* Create `config.json` in this directory.
* Copy and paste the script provided below.
  *  `config_url`: configuration url
  *  `private_key`: private key
  *  `mez_lib_id`: mezzanine library id
  *  `movieCLIP_json_path`: path to `movieCLIP_dataset.json`
  *  `clip_json_path`: path to the output JSON `clip.json`
  *  `utilities_path`: path to `/elv-utils-js/utilities`
```
{
    "config_url": "URL for the configuration",
    "private_key": "Private key",
    "mez_lib_id": "Mezzanine library ID",
    "movieCLIP_json_path": "/path/to/movieCLIP.json",
    "clip_json_path": "/path/to/clip.json",
    "utilities_path": "/path/to/utilities"
}
```

## Command
```
python bulk_tagging.py
```

## Tagging process
* Extract all object IDs from the mezzanine library. 
* Generate a `clip.json` for each object ID and apply tags to the corresponding object on the Fabric.

## Sample Output
* `clip.json`
```
{
    "iq__yiLobFRbwd3d5ZsSV3TtC3wJVoV": {
        "label": "Event - ALL",
        "tags": [
            {
                "start_time": 0,
                "end_time": 15974,
                "text": "corridor (0.0769)"
            },
            {
                "start_time": 0,
                "end_time": 15974,
                "text": "closet (0.0766)"
            },
            {
                "start_time": 0,
                "end_time": 15974,
                "text": "makeup studio (0.0763)"
            },
            {
                "start_time": 0,
                "end_time": 15974,
                "text": "salon (0.0587)"
            },
            {
                "start_time": 0,
                "end_time": 15974,
                "text": "bathroom (0.0586)"
            },
            {
                "start_time": 15974,
                "end_time": 25901,
                "text": "lounge (0.1187)"
            },
            {
                "start_time": 15974,
                "end_time": 25901,
                "text": "bedroom (0.111)"
            },
            {
                "start_time": 15974,
                "end_time": 25901,
                "text": "living room (0.1045)"
            },
            {
                "start_time": 15974,
                "end_time": 25901,
                "text": "interrogation room (0.0496)"
            },
            {
                "start_time": 15974,
                "end_time": 25901,
                "text": "room (0.0412)"
            },
            {
                "start_time": 25901,
                "end_time": 30906,
                "text": "banquet (0.2913)"
            },
            {
                "start_time": 25901,
                "end_time": 30906,
                "text": "dining room (0.146)"
            },
            {
                "start_time": 25901,
                "end_time": 30906,
                "text": "kitchen (0.0794)"
            },
            {
                "start_time": 25901,
                "end_time": 30906,
                "text": "salon (0.045)"
            },
            {
                "start_time": 25901,
                "end_time": 30906,
                "text": "morgue (0.0301)"
            },
            {
                "start_time": 30906,
                "end_time": 64940,
                "text": "dining room (0.1143)"
            },
            {
                "start_time": 30906,
                "end_time": 64940,
                "text": "bar (0.071)"
            },
            {
                "start_time": 30906,
                "end_time": 64940,
                "text": "salon (0.059)"
            },
            {
                "start_time": 30906,
                "end_time": 64940,
                "text": "living room (0.0517)"
            },
            {
                "start_time": 30906,
                "end_time": 64940,
                "text": "banquet (0.05)"
            },
            {
                "start_time": 64940,
                "end_time": 72072,
                "text": "bedroom (0.1527)"
            },
            {
                "start_time": 64940,
                "end_time": 72072,
                "text": "lounge (0.1043)"
            },
            {
                "start_time": 64940,
                "end_time": 72072,
                "text": "living room (0.0941)"
            },
            {
                "start_time": 64940,
                "end_time": 72072,
                "text": "room (0.057)"
            },
            {
                "start_time": 64940,
                "end_time": 72072,
                "text": "cockpit (0.0326)"
            },
            {
                "start_time": 72072,
                "end_time": 84293,
                "text": "banquet (0.1315)"
            },
            {
                "start_time": 72072,
                "end_time": 84293,
                "text": "dining room (0.1019)"
            },
            {
                "start_time": 72072,
                "end_time": 84293,
                "text": "lounge (0.0999)"
            },
            {
                "start_time": 72072,
                "end_time": 84293,
                "text": "living room (0.0845)"
            },
            {
                "start_time": 72072,
                "end_time": 84293,
                "text": "balcony (0.0743)"
            },
            {
                "start_time": 84293,
                "end_time": 92759,
                "text": "bedroom (0.1757)"
            },
            {
                "start_time": 84293,
                "end_time": 92759,
                "text": "lounge (0.0717)"
            },
            {
                "start_time": 84293,
                "end_time": 92759,
                "text": "living room (0.0679)"
            },
            {
                "start_time": 84293,
                "end_time": 92759,
                "text": "closet (0.0571)"
            },
            {
                "start_time": 84293,
                "end_time": 92759,
                "text": "room (0.0564)"
            },
            {
                "start_time": 92759,
                "end_time": 117159,
                "text": "dining room (0.2423)"
            },
            {
                "start_time": 92759,
                "end_time": 117159,
                "text": "banquet (0.2163)"
            },
            {
                "start_time": 92759,
                "end_time": 117159,
                "text": "living room (0.0677)"
            },
            {
                "start_time": 92759,
                "end_time": 117159,
                "text": "lounge (0.0658)"
            },
            {
                "start_time": 92759,
                "end_time": 117159,
                "text": "salon (0.0604)"
            },
            {
                "start_time": 117159,
                "end_time": 131340,
                "text": "bar (0.1807)"
            },
            {
                "start_time": 117159,
                "end_time": 131340,
                "text": "dining room (0.1451)"
            },
            {
                "start_time": 117159,
                "end_time": 131340,
                "text": "banquet (0.0662)"
            },
            {
                "start_time": 117159,
                "end_time": 131340,
                "text": "kitchen (0.0542)"
            },
            {
                "start_time": 117159,
                "end_time": 131340,
                "text": "salon (0.0497)"
            },
            {
                "start_time": 131340,
                "end_time": 136636,
                "text": "bedroom (0.2827)"
            },
            {
                "start_time": 131340,
                "end_time": 136636,
                "text": "lounge (0.0523)"
            },
            {
                "start_time": 131340,
                "end_time": 136636,
                "text": "room (0.042)"
            },
            {
                "start_time": 131340,
                "end_time": 136636,
                "text": "car (0.0391)"
            },
            {
                "start_time": 131340,
                "end_time": 136636,
                "text": "living room (0.039)"
            },
            {
                "start_time": 136636,
                "end_time": 137054,
                "text": "closet (0.1334)"
            },
            {
                "start_time": 136636,
                "end_time": 137054,
                "text": "bedroom (0.0669)"
            },
            {
                "start_time": 136636,
                "end_time": 137054,
                "text": "makeup studio (0.064)"
            },
            {
                "start_time": 136636,
                "end_time": 137054,
                "text": "locker room (0.0551)"
            },
            {
                "start_time": 136636,
                "end_time": 137054,
                "text": "salon (0.0546)"
            }
        ]
    }
}
```
