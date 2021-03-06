import argparse
from pytube.exceptions import VideoUnavailable

import src.fatube.yt_downloader as YT
from src.fatube.frames import save_frames
from src.fatube.video_cut import cut_video

ap = argparse.ArgumentParser()
ap.add_argument(
            "-i", "--input",
            required=True,
            help="YT movie ID or path to video to process"
)
ap.add_argument(
            "-a",
            "--audio",
            help="Download audio only",
            action='store_true'
)
ap.add_argument(
            "-b",
            "--bitrate",
            help="Specify the bitrate (62, 128, 160, 192) kbps",
            action='store',
            type=str
)
ap.add_argument(
            "-v",
            "--video",
            help="Download video only",
            action='store_true'
)
ap.add_argument(
            "-va",
            "--video_and_audio",
            help="Download video with audio",
            action='store_true'
)
ap.add_argument(
            "-res",
            "--resolution",
            help='Specify resolution (144p, 240p, 360p, 480p, 720p, 1080p...)',
            action='store',
            type=str
)
ap.add_argument(
            "-f",
            "--frames",
            help="Extracting frames from specific video",
            action='store_true'
)
ap.add_argument(
            "-s",
            "--start",
            help="Slicing video -> start parameter <seconds>",
            action='store',
)
ap.add_argument(
            "-e",
            "--end",
            help="Slicing video -> end parameter <second>",
            action='store',
)
ap.add_argument(
            "-g",
            "--get_title",
            help="Get Youtube video title",
            action='store_true'
)
ap.add_argument(
            "-d",
            "--get_duration",
            help="Get Youtube video duration in format hh:mm:ss",
            action='store_true'
)
args = vars(ap.parse_args())

if __name__ == '__main__':
    try:
        k = YT.YouTubeVideo(args['input'], YT.VIDEO_FORMAT)
        #print(k.get_video_title())
        #print(k.get_video_duration())
        if args['audio'] and args['bitrate']:
            k.download_audio(args['bitrate'])
        elif args['audio']:
            k.download_audio()
        elif args['audio'] and args['bitrate']:
            k.download_audio(args['bitrate'])
        elif args['video'] and args['resolution']:
            print(args['resolution'])
            k.download_video(args['resolution'])
        elif args['video']:
            k.download_video()
        elif args['video_and_audio'] and args['resolution']:
            k.download_video_with_audio(args['resolution'])
        elif args['get_title']:
            print(k.get_video_title())
        elif args['get_duration']:
            print(k.get_video_duration())
        else:
            k.download_video_with_audio()
    except (VideoUnavailable, NotADirectoryError) as e:
        path_to_video = args['input']
        if args['frames']:
            save_frames(args['input'])
        elif args['start'] and args['end']:
            cut_video(args['input'], int(args['start']), int(args['end']))
