import os
import shutil
source = "D:/pythonSegregation"
dest = "D:/afterSegregation"
list_files = os.listdir(source)
print(list_files)
for fileName in list_files:
    name,ext=os.path.splitext(fileName)
    if ext =="":
        continue
    if ext in[".gif",".pdf",".png",".jpg",".txt"]:
        path1 = source + '/' + fileName
        path2 = dest + '/' + 'imageFiles'
        path3 = dest + '/' + 'imageFiles'+'/'+ fileName
        if os.path.exists(path2):
            print("moving")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving")
            shutil.move(path1,path3)
            
