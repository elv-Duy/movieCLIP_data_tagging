# movieCLIP_data_tagging
A bulk tagging script for the ingested MovieCLIP media on the Eluvio Content Fabric.

## MovieCLIP Tags
* Download the complete list of MovieCLIP Tags from this [Drive Link](https://drive.google.com/file/d/15EhA0BT3IF0EuLP1yXr5nn5ad9soxxox/view).
* Each video in MovieCLIP Tags averages 2 minutes in length and typically segmented into 10 to 100 shots tagged with the top 5 labels based on confidence scores.
* More details on MovieCLIP Tags can be found [here](https://github.com/usc-sail/mica-MovieCLIP/blob/main/split_files/README.md).

## Installation
* [Python](https://github.com/pypa/pip)

```
git clone https://github.com/eluv-io/elv-utils-js
cd elv-utils-js
git checkout mez-video-tag
npm install
```

## Configuration Setup
* Create `config.json` in this directory.
* Copy and paste the script provided below.

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
            }, ...
```


## Sample Output

<img width="1322" alt="Screenshot 2024-07-08 at 3 00 45 PM" src="https://github.com/elv-Duy/movieCLIP_data_tagging/assets/171614703/b93f3f31-172a-4565-ac2e-3ef062b33126">
