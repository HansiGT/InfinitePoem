import os
import argparse

from pydub import AudioSegment

for (dirpath, dirnames, filenames) in os.walk("tracks/"):
    for filename in filenames:
        filepath = dirpath + '/' + filename
        try:
            l_track = AudioSegment.from_file(filepath).pan(-1)
            lm_track = AudioSegment.from_file(filepath).pan(-0.5)
            rm_track = AudioSegment.from_file(filepath).pan(0.5)
            r_track = AudioSegment.from_file(filepath).pan(1)
            l_filename = "L_" + filename
            lm_filename = "LM_" + filename
            rm_filename = "RM_" + filename
            r_filename = "R_" + filename
            l_path = dirpath + '/' + l_filename
            lm_path = dirpath + '/' + lm_filename
            rm_path = dirpath + '/' + rm_filename
            r_path = dirpath + '/' + r_filename
            print('CONVERTING: ' + str(filepath))
            file_handle = l_track.export(l_path, format='wav')
            file_handle = lm_track.export(lm_path, format='wav')
            file_handle = rm_track.export(rm_path, format='wav')
            file_handle = r_track.export(r_path, format='wav')
        except:
            print("ERROR CONVERTING " + str(filepath))
