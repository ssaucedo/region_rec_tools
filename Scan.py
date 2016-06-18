#!/usr/bin/python3
import numpy as np
import modules.cargaAudio as ca
from scipy.io import wavfile
import os


class Region:
    def __init__(self, name,path_to_files):
        self.name = name
        self.path = path_to_files
        self.wav_files_id_list = []
        self.audio_char_list = []
    def add_audio_char(self,audio_c):
        self.audio_char_list.append(audio_c)
    def set_wav_files_id_list(self,RList):
        self.wav_files_id_list = RList

def load_wav_file( file_path , file_namme ):
    Fs, dat = wavfile.read(file_path + file_namme)
    return Fs, dat


def retrieveCorporas(corpus_name,corpus_path,regions):
        original_dir = os.getcwd()
        os.chdir(corpus_path)
        reg = Region(corpus_name,corpus_path)
        for root, dirs, filenames in os.walk(os.getcwd()):
            reg.set_wav_files_id_list(filenames)
            regions.append(reg)
        os.chdir(original_dir)
        return regions

chinese_dir = ""
english_dir = ""

regions = []
regions = retrieveCorporas("chinese",chinese_dir,regions)
regions = retrieveCorporas("english",english_dir,regions)

p = 0
n = 0
for file_name in regions[n].wav_files_id_list:
         Fs, dat = load_wav_file(regions[n].path, file_name)
         p = p + len(dat)
print(p/(len(regions[n].wav_files_id_list)))
