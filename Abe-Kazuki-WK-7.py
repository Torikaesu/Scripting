'''
Searching for Images with PIL
Kazuki Abe

October 2026
'''

import sys
import os
from PIL import Image   # pip install pillow
from prettytable import PrettyTable # pip install prettytable

tbl = PrettyTable(['File', 'Ext', 'Format', 'Width', 'Height', 'Mode'])

print("\nWeek 7 Starter Script\n")
while True:
    targetFolder = input("\nFolder to Examine Q to Quit: ")
    if targetFolder.lower() == 'q':
        break   # breaks loop
    if not os.path.isdir(targetFolder): # checks if it's a folder
        print("Path provided is not a Folder")
        continue
    for currentRoot, dirList, fileList in os.walk(targetFolder):
        for nextFile in fileList:
            fullPath = os.path.join(currentRoot, nextFile)
            absPath = os.path.abspath(fullPath)
            if os.path.isfile(absPath):
                ext = os.path.splitext(absPath)[1]
                try:
                    with Image.open(absPath) as im:
                        tbl.add_row([absPath, ext, im.format, im.size[0], im.size[1], im.mode]) # adds to table, im.size[0] = width im.size[1] = height
                except Exception as err:
                    print("File is not a known Image Type: ", absPath)
                    tbl.add_row([absPath, ext, "[NA]", "[NA]", "[NA]", "[NA]"]) # collects what can be collectd
                    pass
            else:
                print("Path Provided is Not a File")
    tbl.align = 'l'
    print(tbl.get_string(sortby="Format"))
    tbl.clear_rows()    # added since the script doesnt end until quit. This way table will be new every time
print("Script Done")
        