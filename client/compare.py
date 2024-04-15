#compare the content of files in Test with the files in temp with the same name

import os
import glob
import json

#compare file 
def compare_files(file1:str , file2:str):
    with open(file1 , "rb") as f1:
        with open(file2 , "rb") as f2:
            data1 = f1.read()
            data2 = f2.read()
            if data1 == data2:
                return True
            else:
                return False
            

files = glob.glob("Test/*")
temp_files = glob.glob("temp/*")

for file in files:
    for temp_file in temp_files:
        if os.path.basename(file) == os.path.basename(temp_file):
            if compare_files(file , temp_file):
                print(f"{file} is equal to {temp_file}")
            else:
                print(f"{file} is not equal to {temp_file}")
            break
    else:
        print(f"{file} is not in temp directory")