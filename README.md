# movieCLIP_data_tagging
This repository contains a script for bulk tagging the ingested MovieCLIP media on the Eluvio Content Fabric. In MovieCLIP tags, each video is about 2 minutes in length, typically segmented into 10 to 100 shots annotated with the top 5 labels based on confidence scores.

## MovieCLIP Tags
* Download the complete list of MovieCLIP Tags from this [Drive Link](https://drive.google.com/file/d/15EhA0BT3IF0EuLP1yXr5nn5ad9soxxox/view).
* More details on MovieCLIP Tags can be found [here](https://github.com/usc-sail/mica-MovieCLIP/blob/main/split_files/README.md).

## Installation
* Download package `elv-utils-js`
```
git clone https://github.com/eluv-io/elv-utils-js
cd elv-utils-js
git checkout mez-video-tag
npm install
```

## config.json
* Create a file named `config.json` in the directory where `bulk_tagging.py` is located.
* Copy the script provided below and paste it into your `config.json`. Replace `YOUR_PRIVATE_KEY` and `YOUR_PATH` with your specific information.
  *  `private_key`: your private key
  *  `path_to_movieCLIP_json`: path to `movieCLIP_dataset.json` (e.g. `"./movieCLIP_dataset.json"`)
  *  `path_to_tagging_json`: path to the output JSON `tagging.json` (e.g. `"./tagging.json"`)
  *  `path_to_utilities`: path to `/elv-utils-js/utilities` (e.g. `"./elv-utils-js/utilities"`)
  *  `path_from_utilities_to_tagging_json`: path from `/elv-utils-js/utilities` to `tagging.json` (e.g. `"../../tagging.json"`)
```
{
    "config_url": "https://main.net955305.contentfabric.io/config",
    "private_key": "YOUR_PRIVATE_KEY",
    "mez_lib": "ilib4JvLVStm2pDMa89332h8tNqUCZvY",
    "path_to_movieCLIP_json": "YOUR_PATH",
    "path_to_tagging_json": "YOUR_PATH",
    "path_to_utilities": "YOUR_PATH",
    "path_from_utilities_to_tagging_json": "YOUR_PATH"
}
```

## Execute the tagging process
```
python bulk_tagging.py
```


