import os
import shutil

def move_xyt_files(oldpath,newpath):
    for img in os.listdir(oldpath):
        if img.split(".")[-1]=="xyt":
            shutil.copy(os.path.join(oldpath,img),newpath)


if __name__ == "__main__":
    oldpath="/home/gloria/NBIS_python-master/testdatasets/datasets_result/"
    newpath="/home/gloria/NBIS_python-master/testdatasets/datasets_xyt/"
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    move_xyt_files(oldpath, newpath)