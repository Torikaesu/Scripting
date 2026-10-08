'''
Logging meta data and SHA-256 of directory
CYBV 312
Kazuki Abe
October 2026
'''

# Python Standard Libaries 
import os
import re
import logging
import platform
import socket
import uuid
import hashlib # for SHA 256
import time # for times
import datetime # for time conversion

import psutil  # pip install psutil

def getSystemInfo():
    try:
        info={}
        info['platform']=platform.system()
        info['platform-release']=platform.release()
        info['platform-version']=platform.version()
        info['architecture']=platform.machine()
        info['hostname']=socket.gethostname()
        info['ip-address']=socket.gethostbyname(socket.gethostname())
        info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
        info['processor']=platform.processor()
        info['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
        return info
    except Exception as e:
        logging.exception(e)
        return False

def main():
    
    # Remove any old logging script
    if os.path.isfile('Abe-Kazuki-WK-6.txt'):          # REPLACE YOURNAME with Your Name
        os.remove("Abe-Kazuki-WK-6.txt")
    
    # configure the python logger, Replace YOURNAME
    logging.basicConfig(filename='Abe-Kazuki-WK-6.txt', level=logging.DEBUG, format='%(process)d-%(levelname)s-%(asctime)s %(message)s')
    logging.info("Script Start\n")
    
    investigator = input("Investigator Name:  ")            # Enter Your Name at this prompt
    organization = input("Class Code       :  ")            # Enter the Class at this prompt i.e. CYBV-312 YOUR SECTION
    purpose = input("Purpose          :  ")                 # Enter the purpose of the scan

    logging.info("Investigator:   " + investigator)
    logging.info("Class Code  :   " + organization)
    logging.info("Purpose     :   " + purpose)              # added purpose like in example log
    logging.info("=" * 40 + "\n")                           # creates a border
    
    sysInfo = getSystemInfo()

    if sysInfo:
        ''' YOUR CODE GOES HERE 
            Write all collected information to the log file
        '''  
        logging.info("***** System Information *****")      # header
        for key, value in sysInfo.items():
            logging.info("\t" + key + ": " + str(value))
        logging.info("=" * 40 + "\n")                       # creates a border
    else:
        logging.error("Unable to collect stystem information")

    while True:                                             # stops the loop if a Directory doesn't exist
        targetDir = input("Directory to scan: ")
        if os.path.isdir(targetDir):
            break
        print("Unable to find Directory")

    logging.info("Specified Directory" + targetDir + "\n")  # tells tyhe directory name

    startTime = time.time()                                 # starts tracking time
    count = 0                                               # starts counting

    for currentRoot, dirs, files in os.walk(targetDir):     # walks the folder and all subfolders
        for nextFile in files:
            try:                                            # error handeling
                fullPath = os.path.join(currentRoot, nextFile)
                absPath = os.path.abspath(fullPath)
            
                stats = os.stat(absPath)
            
                fileSize = stats.st_size
                modified = stats.st_mtime
                accessed = stats.st_atime
                created = stats.st_ctime
            
                modifiedHuman = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(modified))   # human readable modified time
                accessedHuman = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(accessed))   # human readable access time
                createdHuman = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(created))     # human readable creation time

                with open(absPath, 'rb') as target:         # opens the file in binary using the absolute file path
                    fileContents = target.read()            # reads the file into memory
                    sha256Obj = hashlib.sha256()            # starts the hash import
                    sha256Obj.update(fileContents)          # points it to the file loaded in memory
                    hashVal  = sha256Obj.hexdigest()        # converts the file into hex digest

                logging.info("File Proccessed: ")
                logging.info("\t Path: " + absPath)
                logging.info("\t File Size: " + format(fileSize, ','))
                logging.info("\t Last Modified: " + modifiedHuman)
                logging.info("\t Last Accessed: " + accessedHuman)
                logging.info("\t Created:       " + createdHuman)
                logging.info("\t SHA-256:       " + hashVal)
                logging.info("=" * 40 + "\n")               # creates a border
                count += 1                                  # adds to the count
            except Exception as e:
                logging.error("Fail:    " + nextFile + "Exception = ", str(e))

    endTime = time.time()                                   # stops tracking time
    elapsedTime = int(endTime - startTime)
    delta = datetime.timedelta(seconds=elapsedTime)         # gets the elapsed time of the script
    logging.info("Elapsed Time: " + str(delta))
    logging.info("Files Proccessed: " + str(count))
    logging.info("Script Ended")


if __name__ == '__main__':
    
    print("\n\nWeek-6 Logging Starter Script - Abe Kazuki \n")
    main()
    print("\nScript End")

