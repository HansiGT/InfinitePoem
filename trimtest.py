import os
import argparse

from pydub import AudioSegment
from pydub.silence import detect_leading_silence
from pydub.playback import play

for (dirpath, dirnames, filenames) in os.walk("tracks (uncut)2/"):
    for filename in filenames:
        filepath = dirpath + '/' + filename
        track = AudioSegment.from_file(filepath)
        x = - (len(track) - detect_leading_silence(track, 0.01))
        track1 = track[x:]
        y = len(track) - detect_leading_silence(track.reverse(), 0.01)
        track2 = track1[:y]
        print('TRIMMING: ' + str(filepath))
        play(track2)
