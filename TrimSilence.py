import os
import argparse

from pydub import AudioSegment
from pydub.silence import detect_leading_silence

for (dirpath, dirnames, filenames) in os.walk("tracks (uncut)/"):
    for filename in filenames:
        try:
            filepath = dirpath + '/' + filename
            track = AudioSegment.from_file(filepath)
            x = - (len(track) - detect_leading_silence(track, -35)) - 80
            track1 = track[x:]
            y = len(track1) - detect_leading_silence(track1.reverse(), -35) + 80
            track2 = track1[:y]
            print('TRIMMING: ' + str(filepath))
            file_handle = track2.export(filepath, format='wav')
        except:
            print("ERROR TRIMMING " + str(filepath))
