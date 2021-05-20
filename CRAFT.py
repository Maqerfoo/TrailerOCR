import easyocr
import os
import cv2
import numpy as np
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_folder")
args = parser.parse_args()


reader = easyocr.Reader(['en'], recognizer = False, gpu = False)
try: 
    os.mkdir('CRAFT_output') 
except OSError as error: 
    pass
output_path = os.path.join(os.getcwd(), "CRAFT_output")

rootdir = os.path.join(os.getcwd(), args.input_folder)

for subdir, dirs, files in os.walk(rootdir):
    files.sort()
    for file in files:
        img = cv2.imread(os.path.join(subdir, file))
        print("detecting on " + file)
        tic = time.perf_counter()
        result = reader.detect(img, width_ths = 0.12)
        toc = time.perf_counter()
        print(f"Time to detect was {toc - tic:0.4f} seconds")
        f = open(os.path.join(output_path, os.path.splitext(file)[0] + ".txt"), "w")
        for text in result[0]:
            cv2.rectangle(img , (text[0],text[3]) , (text[1],text[2]) , (0,255,0) , 3)
            free_form = [text[0],text[2],text[1],text[2],text[1],text[3],text[0],text[3]]
            f.write("\n")
            f.write(",".join(map(str, free_form)))
        cv2.imwrite(os.path.join(output_path, file), img)