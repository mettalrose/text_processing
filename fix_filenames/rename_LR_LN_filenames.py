#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys  # imports the library for command line
import re  # imports the library for regular expressions
import glob  # imports the library for seeing all files
import os  # imports the library for opening and writing files
from shutil import copyfile  # library for system operations

# Given a file located in a specific folder path,
# rename the file using the path elements
# The command syntax is as follows:
# python repository_file_names.py path
# Example (with actual test folder)
# python repository_file_names.py 106i


def splitall(path):
    """ Given a relative directory path, split out each directory into a list """
    allparts = []
    while 1:
        parts = os.path.split(path)
        if parts[0] == path:  # sentinel for absolute paths
            allparts.insert(0, parts[0])
            break
        elif parts[1] == path:  # sentinel for relative paths
            allparts.insert(0, parts[1])
            break
        else:
            path = parts[0]
            allparts.insert(0, parts[1])
    return allparts


## Auto-increment starting point
counter = 1439
if __name__ == '__main__':  # iniitalizes the main block of code
    if len(sys.argv) > 1:  # 1st element is script name and other elements follow
        for arg in sys.argv[1:]:  ## for every argument in the list of arguments
            for dirpath, dirnames, files in os.walk(arg):
                for name in files:        
                    fullpath = os.path.join(dirpath, name)
                    #print('Full path:', fullpath)
                    #x = input('press enter to continue')
                    if not os.path.isfile(fullpath):
                        sys.exit('No file found at', fullpath, '. Please try again.')
                        
                    ## Get the original filename
                    filename = os.path.basename(name)
                    print("Original file: ", filename)
                    if '.txt' in filename:
                        directory = dirpath
                        #print("Original path: ", dirpath)
                        filename_base, file_extension = os.path.splitext(filename)
                        #print('File extension:', file_extension)
                        #x = input('press enter to continue')
                        directory_parts = splitall(dirpath)
                        print(directory_parts)
                        #x = input('press enter to continue')
                        draft = directory_parts[1]
                        filename_parts = filename.split("_")
                        filename_parts_new = []
                        for part in filename_parts:
                            if part == "LR":
                                part = part.replace("LR", "LN")
                            filename_parts_new.append(part)
                            #print(filename_parts_new)
                            #x = input('press enter to continue')

                        new_filename = (filename_parts_new[0] + '_' + filename_parts_new[1] + '_' + filename_parts_new[2] + '_' + filename_parts_new[3] + "_" + filename_parts_new[4] + "_" + filename_parts_new[5] + "_" + filename_parts_new[6]+ "_" + filename_parts_new[7])
                        print("new filename: ", new_filename)
                        #x = input('press enter to continue')
                        
                        cwd = os.getcwd()
                        newpath = os.path.join(cwd, 'filenames', "LN", draft)
                        os.makedirs(newpath, exist_ok=True)
                        print("new path: ", newpath)
                        #x = input('press enter to continue')
                        ## Defines new file, with same folder location
                        output_file = os.path.join(newpath, new_filename)
                        ## Moves the original file to the newly named file
                        copyfile(fullpath, output_file)
