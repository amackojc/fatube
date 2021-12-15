#!/usr/bin/python

import argparse
import os
from os import path
from DownloaderHelpers import YTHelper

import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
                help="path to input video folder")
args = vars(ap.parse_args())


def save_frames(path_to_video, color = False):
    cap = cv2.VideoCapture(path_to_video)
    current_frame = 0
    #frames_path = '/'.join(path_to_video.split('\\')[:-1]) + '/FRAMES'
    #if not path.exists(frames_path):
    #    os.mkdir(frames_path)
    base = os.path.basename(path_to_video)
    basename = os.path.splitext(base)[0]
    directory_name = os.path.dirname(path_to_video)
    frames_path = f'{directory_name}/FRAMES/{basename}'
    YTHelper.prepare_directory(frames_path)
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            if not color:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                name = f"frame_{current_frame}.jpg"
                print(f"Creating frame in gray... {name}")
                cv2.imwrite(os.path.join(frames_path , name), gray)
            else:
                name = f"frame_{current_frame}.jpg"
                print(f"Creating frame in color... {name}")
                cv2.imwrite(os.path.join(frames_path , name), frame)
        else:
            break
        current_frame += 1
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    save_frames(args['input'], True)
