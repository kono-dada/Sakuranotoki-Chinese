import shutil
import os
path = ".\\script\\"
des = "..\\樱之刻\\script\\"
filelist = os.listdir(path)
for i in filelist:
    try:
        shutil.copyfile(path + i, des + i)
        print("Successfully copied " + i)
    except IOError as e:
        print("Copy " + i + "failed.")
        print(e)
    except:
        print("Copy " + i + "failed.")