import numpy as np
from scipy.io import wavfile
import os
import sys

global_audio_folder = '/corpora'

def load_wav_file( region_name , file_id_number ):
    os.chdir("D:\\UADE\\PFI_workspace\\TestMultilingual\\corpora\\")
    Fs, dat = wavfile.read(region_name+'/256K/'+ file_id_number)
    normDat = normalize_audio( dat ).astype(float)
    return Fs, normDat


def iterateAndValidateFs(file_path,fs):

    for i in os.listdir(file_path):
            wav_path = file_path + "/" + i
            Fs , dat = wavfile.read(wav_path)
            if(Fs != fs): print("Wrong Fs!, check "   + str(wav_path))
    return os.getcwd()

iterateAndValidateFs("pathToWavFilesFolder",16000)
