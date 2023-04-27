import os
import shutil
import re
import numpy as np
import torch as tc
import torchvision as tv
from PIL import Image
from skimage import io
import pandas as pd

def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]


create_folder("DATA/training/No_homm")
create_folder("DATA/training/Homm")

create_folder("DATA/test/No_homm")
create_folder("DATA/test/Homm")

path_t = 'DATA'

numer = 0

path_to_dataset = f'..\\..\\Desktop\\ProjektTOM\\CT'

zbiory = ['test', 'training']
klasy = ['Homm', 'No_homm']

horr = tv.transforms.RandomHorizontalFlip(1.0)
vert = tv.transforms.RandomVerticalFlip(1.0)
rott = tv.transforms.RandomRotation( degrees= (180,180))
from os import listdir
from os.path import isfile, join
for zbior in zbiory:
    print(zbior)
    for klasa in klasy:
        path = join(path_to_dataset, zbior, klasa)
        for f in listdir(path):
            p = join(path, f)
            
            if klasa == 'Homm':
                img = Image.open(p)
                
                file_horr = f.replace('.jpg', '_horr.jpg')
                path_to = join(path_t, zbior, klasa, file_horr)
                horr(img).save(path_to)

                file_vert = f.replace('.jpg', '_vert.jpg')
                path_to = join(path_t, zbior, klasa, file_vert)
                vert(img).save(path_to)

                file_rott = f.replace('.jpg', '_rott.jpg')
                path_to = join(path_t, zbior, klasa, file_rott)
                rott(img).save(path_to)

                path_to = join(path_t, zbior, klasa, f)
                img.save(path_to)
            else:
                source_img = p
                dest_img = join(path_t, zbior, klasa, f)
                shutil.copy(source_img, dest_img)
            numer+=1
            print(numer)