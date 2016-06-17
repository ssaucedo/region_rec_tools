import numpy as np
from scipy.io import wavfile
import os
import sys

global_audio_folder = '/corpora'

def iterateAndValidateFs(file_path,fs):

    for i in os.listdir(file_path):
            wav_path = file_path + "/" + i
            Fs , dat = wavfile.read(wav_path)
            if(Fs != fs): print("Wrong Fs!, check "   + str(wav_path))
    return os.getcwd()

iterateAndValidateFs("pathToWavFilesFolder",16000)
