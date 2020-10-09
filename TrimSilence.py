import os
import argparse

from pydub import AudioSegment
from pydub.silence import detect_leading_silence

for (dirpath, dirnames, filenames) in os.walk("tracks (uncut)2/"):
    for filename in filenames:
        filepath = dirpath + '/' + filename
        try:
            track = AudioSegment.from_file(filepath)
            x = - (len(track) - detect_leading_silence(track, 0.01))
            track = track[x:]
            y = len(track) - detect_leading_silence(track.reverse(), 0.01)
            track = track[:y]
            print('TRIMMING: ' + str(filepath))
            file_handle = track.export(filepath, format='wav')
        except:
            print("ERROR TRIMMING " + str(filepath))
