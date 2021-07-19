import os
import shutil
path="/Users/aries/Desktop/python/clas99"
print("before copying the file")
print(os.listdir(path))
source="/Users/aries/Desktop/python/clas99/main.txt"
destination="/Users/aries/Desktop/python/clas99/main2.txt"
dest=shutil.copy(source, destination)
print("after copying the file")
print(os.listdir(path))
