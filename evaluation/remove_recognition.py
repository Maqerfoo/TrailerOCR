from zipfile import *
import shutil
import os

source_subm = ZipFile('submit.zip', 'r')
source_subm.extractall('submit')
source_subm.close()
subm_filelist = os.listdir('submit')
os.makedirs('new')
for file in subm_filelist:
    f = open('submit/' + file, "r")
    f_new = open("new/" + file, "w")
    lines = f.readlines()
    for line in lines:
        newline = ",".join(line.split(",")[:8])
        print(newline)
        f_new.write(newline)
        f_new.write("\n")
shutil.rmtree('submit')