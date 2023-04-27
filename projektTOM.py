import pandas as pd
import os
import shutil
import re




def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]


def path_to_brain(num):
    s = '0'+str(num)
    s = s[-3:-1]+s[-1]
    return f'computed-tomography-images-for-intracranial-hemorrhage-detection-and-segmentation-1.0.0\\Patients_CT\\{s}\\brain'





df = pd.read_csv("computed-tomography-images-for-intracranial-hemorrhage-detection-and-segmentation-1.0.0/hemorrhage_diagnosis.csv")

create_folder("CT_images")

create_folder("Labels")

path_to = 'CT_images'

annotations = pd.DataFrame(columns = ['photo_nr', 'target'])
for num in range(49,131):
    path = path_to_brain(num)
    _ ,_,files = next(os.walk(path))
    n = 1
    files.sort(key=natural_keys)
    for f in files:
        
        if f == f'{n}.jpg':
            
            f_to = f'{num}_{f}'
            source_img = os.path.join(path, f)
            dest_img = os.path.join(path_to, f_to)
            if os.path.exists(dest_img):
                annotations.loc[len(annotations)] = [f'{path_to}\\{f_to}', df.loc[(df['PatientNumber']==num) & (df['SliceNumber']==n)]['No_Hemorrhage'].values[0]] 
                #print(df.loc[(df['PatientNumber']==num) & (df['SliceNumber']==n)]['No_Hemorrhage'].values)
                pass

            else:
                shutil.copy(source_img, dest_img)
                #annotations.loc[len(annotations)] = [f_to, df.loc[(df['PatientNumber']==num) & (df['SliceNumber']==n)]['No_Hemorrhage']]  
                 
            n+=1
        else:
            pass
annotations.to_csv('Labels\classes.csv')
    
        











