import argparse
from yt_downloader import YouTubeVideo
from frames import save_frames
from video_cut import cut_video

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", required=True,
                help="path to text file with video ID's or single YouTube video ID")
parser.add_argument("--cut", "--input", help='cutting video')
parser.add_argument("--color", help="saves frames in color")
# parser.add_argument("--help", help="print user manual")

args = parser.parse_args()