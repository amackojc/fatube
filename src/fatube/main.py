import argparse
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
ffmpeg_extract_subclip("video1.mp4", start_time, end_time, targetname="test.mp4")



parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", required=True,
                help="path to text file with video ID's or single YouTube video ID")
parser.add_argument("--cut", "--input", help)
parser.add_argument("--color", help="saves frames in color")
parser.add_argument("--help", help="print user manual")

args = parser.parse_args()