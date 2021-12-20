import pytest
import os

from fatube.yt_downloader import YouTubeVideo
#from fatube.skeleton import fib, main

__author__ = "Aleksander Mackojć"
__copyright__ = "Aleksander Mackojć"
__license__ = "MIT"


#def test_fib():
#    """API Tests"""
#    assert fib(1) == 1
#    assert fib(2) == 1
#    assert fib(7) == 13
#    with pytest.raises(AssertionError):
#        fib(-10)

def test_YT_get_duration_time():
    YT_test_first = YouTubeVideo('oC3fhUjg30E','mp4')
    YT_test_second = YouTubeVideo('Y9dr2zw-TXQ','mp4')
    YT_test_third = YouTubeVideo('c6zJ7fJ5fKs','mp4')
    assert YT_test_first.get_video_duration() == '1:52:48'
    assert YT_test_second.get_video_duration() == '0:02:38'
    assert YT_test_third.get_video_duration() == '0:15:06'

def test_YT_get_title():
    YT_test_first = YouTubeVideo('oC3fhUjg30E','mp4')
    YT_test_second = YouTubeVideo('Y9dr2zw-TXQ','mp4')
    YT_test_third = YouTubeVideo('c6zJ7fJ5fKs','mp4')
    assert YT_test_first.get_video_title() == "Dr. David Berson: Your Brain's Logic & Function | Huberman Lab #50"
    assert YT_test_second.get_video_title() == 'Fantastic Beasts: The Secrets of Dumbledore – Official Trailer'
    assert YT_test_third.get_video_title() == 'The Witcher in 15 Minutes | Netflix'

def test_YT_download_video():
    YT_test = YouTubeVideo('Y9dr2zw-TXQ','mp4')
    YT_test.download_video()
    checker = os.path.exists('Y9dr2zw-TXQ/VIDEOS/Fantastic Beasts: The Secrets of Dumbledore – Official Trailer_480p.mp4')
    assert checker == True

def test_YT_download_audio():
    YT_test = YouTubeVideo('Y9dr2zw-TXQ','mp4')
    YT_test.download_audio()
    checker = os.path.exists('Y9dr2zw-TXQ/AUDIO/Fantastic Beasts: The Secrets of Dumbledore – Official Trailer_160kbps.mp3')
    assert checker == True
