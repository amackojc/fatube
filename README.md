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

`pip install -r requirements.txt`



## Usage
### Examples of usage:

#### Download video with audio in resolution of 480p.

`python main.py -i xcJtL7QggTI -res 480p`

#### Download video without audio in default resolution.

`python main.py -i xcJtL7QggTI -v`

#### Download audio in bitrate of 128kbps.

`python main.py -i xcJtL7QggTI -a -b 128`




## Room for Improvement
- Downloading many videos based on their ID's stored in single .txt file

<!-- Optional -->
<!-- ## License -->
<!-- This project is open source and available under the [... License](). -->

<!-- You don't have to include all sections - just the one's relevant to your project -->
