# FATube
> FATube is a tool for downloading and processing videos from YouTube.


## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Room for Improvement](#room-for-improvement)
<!-- * [License](#license) -->


## General Information
FATube is a tool for downloading and processing videos from YouTube.

It aim is to ease the process of preparing datasets for machine learning algorithms.


## Technologies Used
- Python 3
- PyTube
- MoviePy
- OpenCV


## Features
- Automatic creation of folder structure
- Choice of download type (video with audio / video without audio / only audio)
- Choice of resolution, in which video should be downloaded
- Choice of bitrate for downloaded audio 
- Saving frames of video (in color or gray format)
- Cutting videos


## Screenshots
Example folder structure after usage.

![Example screenshot](/docs/screenshots/example_folder_structure.PNG?raw=true)
<!-- If you have screenshots you'd like to share, include them here. -->


## Setup
To run the program you need to install required packages.
All of them are listed in docs/requirements.txt
To install them use:

`pip install -r docs/requirements.txt`

And you can use everyhing "from your finger"

or you can build it using PyScaffold

1. Prepare your virtual enviroment using [virtualenv](https://docs.python.org/3/library/venv.html)
2. Install requirements using `pip install -e .`
3. Build documenation `tox -e docs`
4. Build packages `tox -e build`
5. Run tests in prepared enviroment `tox`

After this few points your enviroment will be fully prepared to use every script


## Usage
### Examples of usage:

#### Download video with audio in resolution of 480p.

`python main.py --input <youtbue_id> --resolution 480p`

#### Download video without audio in default resolution.

`python main.py --input <youtbue_id> --video`

#### Download audio in bitrate of 128kbps.

`python main.py --input <youtbue_id> --audio --bitrate 128`

#### Get Youtube video duration time

`python main.py --input <youtbue_id> --get_duration`

#### Get Youtube video title

`python main.py --input <youtbue_id> --get_title`

#### Extract all frames from specific video

`python main.py --input <path_to_video_file> --frames`

#### Cut the video clip

`python main.py --input <path_to_video_file> --start <seconds> --end <seconds>`


## Room for Improvement
- Downloading many videos based on their ID's stored in single .txt file
- Create few others flags for better functionality (for exmaple: color video choice)

<!-- Optional -->
<!-- ## License -->
<!-- This project is open source and available under the [... License](). -->

<!-- You don't have to include all sections - just the one's relevant to your project -->
