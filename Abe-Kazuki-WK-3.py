'''
Script: Meta Data and Hash Finder
Author: Kazuki Abe
Date: September 2026
Purpose: The script will collect the meta data and associated hash value of all files within a given directory
'''

# Python Standard Libaries 
import os       # for directory traversal
import hashlib  # for getting hash values
import time     # for convertine epoch time to human readable

# Python 3rd Party Libraries
from prettytable import PrettyTable     # pip install prettytable

# Psuedo Constants

targetFolder = input("Enter Target Folder: ")
# Start of the Script
print("Walking: ", targetFolder, "\n")

tbl = PrettyTable(['AbsPath','FileSize','LastModified','LastAccess','CreatedTime','SHA-256'])  

for currentRoot, dirList, fileList in os.walk(targetFolder):

    for nextFile in fileList:
            
        fullPath = os.path.join(currentRoot, nextFile)  # Gets file path
        absPath  = os.path.abspath(fullPath)            # Gets absolute file path

        try:    # allows for error handeling

            fileSize = os.path.getsize(absPath)             # Gets the file size using the absolute path
            modified = os.path.getmtime(absPath)            # Getthe files last modified time using the absolute path
            accessed = os.path.getatime(absPath)            # Gets the files last access time using the absolute path
            created  = os.path.getctime(absPath)            # Gets the files creation time usign thew absolute file path

            humanModified = time.ctime(modified)            # converts epoch time to human readable
            humanAccessed = time.ctime(accessed)            # converts the epoch time to human readbale
            humanCreated = time.ctime(created)              # converts the epoch to human readable

            with open(absPath, 'rb') as target:             # opens the file in binary using the absolute file path
                fileContents = target.read()                # reads the file into memory
                sha256Obj = hashlib.sha256()                # starts the hash import
                sha256Obj.update(fileContents)              # points it to the file loaded in memory
                hashVal  = sha256Obj.hexdigest()            # converts the file into hex digest

        except Exception as err:
            print("Fail:    ", absPath, "Exception = ", str(err))  # prints any erros that may happen while collecting meta data and hash per loop
            continue    # continues the loop even if one file may throw an error
        
        tbl.add_row( [ absPath, fileSize, humanModified, humanAccessed, humanCreated, hashVal] ) 



tbl.align = "l" # align the columns left justified
# display the table
print (tbl.get_string(sortby="FileSize", reversesort=True))


print("\nScript-End\n")