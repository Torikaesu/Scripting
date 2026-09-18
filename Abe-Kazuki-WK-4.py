'''
Script: URL finder
Author: Kazuki Abe
Date: September 2026
Purpose: The script will break a file into chunks and find URLs
'''

# Python Standard Libaries 
import os       # for directory traversal
import re       # for RegEx

# Python 3rd Party Libraries
from prettytable import PrettyTable     # pip install prettytable

# Psuedo Constants
urlPattern          = re.compile(b'\w+:\/\/[\w@][\w.:@]+\/?[\w\.?=%&=\-@/$,]*')
chunkSize = 65535
# Start of the Script

urlCounts = {}

tbl = PrettyTable(['OCCURS', 'URL'])  

try:    # allows for error handeling
    targetFile = input("Enter Target Folder: ")
    print("Searching: ", targetFile, "\n")

    if os.path.isfile(targetFile):  # checks that the file exists before starting loop
        print("Proccessing file:    ", targetFile)
        print("in chunks of:    ", chunkSize, "bytes")
        bytesProcessed = 0
        chunkCnt = 0
        with open(targetFile, 'rb') as File:    # opens the file in read binary mode
                while True:
                    fileChunk = File.read(chunkSize)
                    bytesProcessed += len(fileChunk)
                    if fileChunk:  # if we still have data
                        foundUrls = urlPattern.findall(fileChunk)

                        for url in foundUrls:
                            url = url.decode('utf-8', errors='replace') # decodes the RegEx to remove 'b' from dictionary url entries
                            if url in urlCounts:
                                  urlCounts[url] += 1   # if url already exists add to the count
                            else:
                                 urlCounts[url] = 1     # if url doesn't already exist set the count to 1

                        chunkCnt += 1
                    else:
                        # File has been processed
                        print("\nProcessed: ", "{:,}".format(bytesProcessed), "bytes", "in", chunkCnt, "chunks")
                        break


except Exception as err:    # error handeling
    print("\nException: "+str(err)+ "Script Aborted")

for url, count in urlCounts.items():    # takes the count and url from dictionary
    tbl.add_row([count, url])

tbl.align = "l" # align the columns left justified
# display the table
print (tbl.get_string(sortby="OCCURS", reversesort=True))   # sorts the table by number of count


print("\nScript-End\n")