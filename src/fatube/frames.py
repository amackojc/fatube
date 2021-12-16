#!/usr/bin/python

from os import path
import cv2
from src.fatube.DownloaderHelpers import YTHelper


def save_frames(path_to_video, color=True):
    cap = cv2.VideoCapture(path_to_video)
    current_frame = 0
    base = path.basename(path_to_video)
    basename = path.splitext(base)[0]
    directory_name = path.dirname(path_to_video)
    frames_path = f'{directory_name}/FRAMES/{basename}'
    YTHelper.prepare_directory(frames_path)
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            if not color:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                name = f"frame_{current_frame}.jpg"
                print(f"Creating frame in gray... {name}")
                cv2.imwrite(path.join(frames_path, name), gray)
            else:
                name = f"frame_{current_frame}.jpg"
                print(f"Creating frame in color... {name}")
                cv2.imwrite(path.join(frames_path, name), frame)
        else:
            break
        current_frame += 1
    cap.release()
    cv2.destroyAllWindows()
