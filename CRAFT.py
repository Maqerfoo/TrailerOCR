import easyocr
import os
import cv2
import numpy as np

reader = easyocr.Reader(['en'], recognizer = False, gpu = False)
output_path = os.path.join(os.getcwd(), "CRAFT_output")

rootdir = os.path.join(os.getcwd(), "IVtext")

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        img = cv2.imread(os.path.join(subdir, file))
        result = reader.detect(img)
        f = open(os.path.join(output_path, os.path.splitext(file)[0] + ".txt"), "w")
        for text in result[0]:
            cv2.rectangle(img , (text[0],text[3]) , (text[1],text[2]) , (0,255,0) , 3)
            free_form = [text[0],text[3],text[1],text[3],text[0],text[3],text[0],text[2]]
            f.write("\n")
            f.write(",".join(map(str, free_form)))
        cv2.imwrite(os.path.join(output_path, file), img)