#!/usr/bin/python

import os
import datetime

from pytube import YouTube
from helpers.DownloaderHelpers import *

WORKSPACE = os.getcwd()

YOUTUBE_URL = 'https://www.youtube.com/watch?v='
VIDEO_FORMAT = 'mp4'
DEFAULT_RESOLUTION = '480p'


class YouTubeVideo:
    """
        The YouTube object is reponsible for connection with YT
        to download videos or audios and obtain desired information
    """
    def __init__(self, youtube_id, video_format):
        """Initializes needed parameters cloesly related to YT service"""
        self.youtube_id = youtube_id
        self.video_format = video_format
        self.youtube_video = YouTube(YOUTUBE_URL + self.youtube_id)

    def download_video(self, video_resolution=None):
        """ Download the video itself"""
        videos = self.youtube_video.streams.filter(resolution=video_resolution)
        if video_resolution is not None:
            if not check_empty_list_of_candidates(videos):
                download_specific_video(self, videos, video_resolution)
        else:
            print("Downloading...")
            download_specific_video(self, videos, DEFAULT_RESOLUTION)
            print("Done!")

    def download_audio(self, average_bitrate=None):
        """ Download the audio itself"""
        audios = self.youtube_video.streams.filter(only_audio=True)
        if average_bitrate is not None:
            average_bitrate = average_bitrate + 'kbps'

            if (not check_empty_list_of_candidates(audios)
                and check_bitrate_in_candidates(audios, average_bitrate)):
                print("Downloading...")
                audios.filter(abr=average_bitrate)[0] \
                      .download(
                          filename=self.get_video_title() +
                          f'_{average_bitrate}.mp3'
                      )
                print("Done!")
        else:
            highest_birate = str(get_highest_audio_quality(audios)) + 'kbps'
            print("Downloading...")
            audios.filter(abr=highest_birate)[0] \
                  .download(
                      filename=self.get_video_title() +
                      f'_{highest_birate}.mp3'
                  )
            print("Done!")

    def download_video_with_audio(self, video_resolution=None):
        """Download video with audio (if it's avaiable)"""
        videos = self.youtube_video.streams \
                                   .filter(
                                        progressive=True,
                                        resolution=video_resolution
                                    )
        if video_resolution is not None:
            if not check_empty_list_of_candidates(videos):
                download_specific_video(self, videos, video_resolution)
        else:
            print("Downloading...")
            videos.get_highest_resolution() \
                  .download(
                      filename=self.get_video_title() +
                      f'_{videos.get_highest_resolution().resolution}.{VIDEO_FORMAT}'
                  )
            print("Done!")

    def get_video_title(self):
        """Returns YT video title"""
        return self.youtube_video.title

    def get_video_duration(self):
        """Returns duration on YT video"""
        return str(datetime.timedelta(seconds=self.youtube_video.length))


if __name__ == '__main__':
    EXAMPLE_ID = '-mdv2wf8yQ8'
    k = YouTubeVideo(EXAMPLE_ID, VIDEO_FORMAT)
    print(k.get_video_title())
    print(k.get_video_duration())
    k.download_audio()
