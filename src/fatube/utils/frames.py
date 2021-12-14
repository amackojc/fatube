import argparse
import os

import cv2
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
                help="path to input video folder")
args = vars(ap.parse_args())

def save_frames(path_to_video, color = False):
    cap = cv2.VideoCapture(path_to_video)
    i = 0
    frames_path = path_to_video + '\\frames'
    while (cap.isOpened()):
        ret, frame = cap.read()
        frameId = int(round(cap.get(1)))
        if not color:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(os.path.join(frames_path , 'waka.jpg'), gray)
            i += 1
        else:
            cv2.imwrite(os.path.join(frames_path , 'waka.jpg'), frame)
            i += 1
    cap.release()
    cv2.destroyAllWindows()


def save_frames2(path_to_video, color = False):
    cap = cv2.VideoCapture(path_to_video)
    # if cap.isOpened():
    current_frame = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            if not color:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                name = f"frame_{current_frame}.jpg"
                print(f"Creating frame in gray... {name}")
                cv2.imwrite(name, gray)
            else:
                name = f"frame_{current_frame}.jpg"
                print(f"Creating frame in color... {name}")
                cv2.imwrite(name, frame)
        else:
            break
        current_frame += 1
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    print('XD')
    save_frames2(args['input'])