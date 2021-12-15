import argparse

from moviepy.editor import *

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
                help="path to input video folder")
ap.add_argument("-s", "--start", required=True,
                help="start of slice")
ap.add_argument("-e", "--end", required=True,
                help="end of slice")
args = vars(ap.parse_args())

def cut_video(path_to_video, start_time, end_time):
    clip = VideoFileClip(path_to_video)
    clip = clip.subclip(start_time, end_time)
    clip.write_videofile(f'{path_to_video.replace(".mp4", "")}_cut.mp4')

if __name__ == "__main__":
    cut_video(args['input'], int(args['start']), int(args['end']))