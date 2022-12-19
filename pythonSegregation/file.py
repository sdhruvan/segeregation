import os
import shutil
os.makedir("D:/session111") 
from_dir = source="D:/textconverter"
to_dir = dest="D:/session111"
list_of_files = os.listdir(from_dir)
print(list_of_files)