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

# The CSV file for getting instructor ID is defined, relative to:
csv_filename = "instructors_Arizona.csv"

# Auto-increment starting point
counter = 1224

# function that gets a list with all names in the csv file
# and returns a list with unique names (it eliminated repeated names)


def get_unique_names(list):
    new_list = []  # create new empty list
    for element in list:
        if element not in new_list:
            new_list.append(element)  # add elements that are not in the new list yet
    return new_list

if __name__ == '__main__':  # iniitalizes the main block of code
    if len(sys.argv) > 1:  # 1st element is script name and other elements follow
        if not os.path.isfile(csv_filename):
            sys.exit('No CSV file found. Exiting...')
        # open csv file first, to create hash table/dictionary
        csv_file = open(csv_filename, 'r')  # opens the file as read only (w is write)
        csvhash = {}
        for line in csv_file:  # for every line in the file; can be used for lists as well; can also use counter if you want
            print(line)  # print the lines in the file
            #x = input('press enter to continue')
            cleanline = re.sub('\r?\n', '', line)
            elements_of_line = cleanline.split(',')  # splits on comma (columns in csv file)
            print(elements_of_line)
            #x = input('press enter to continue')
            # create a new list for all names in the csv files
            all_names = []  # create empty list
            all_names.append(elements_of_line[1])  # add first name
            all_names.append(elements_of_line[2])  # add last name
            csvhash[elements_of_line[2]] = {"ID": elements_of_line[0]} #only last name is needed as key

        for arg in sys.argv[1:]:  # for every argument in the list of arguments
            for dirpath, dirnames, files in os.walk(arg):
                for name in files:
                    
                    fullpath = os.path.join(dirpath, name)
                    print('Full path:', fullpath)
                    #x = input('press enter to continue')
                    if not os.path.isfile(fullpath):
                        sys.exit('No file found at', fullpath, '. Please try again.')
                    
                    # Get the original filename
                    filename = os.path.basename(name)
                    print("Original file: ", filename)
                    directory = dirpath
                    print("Original path: ", dirpath)
                    filename_base, file_extension = os.path.splitext(filename)
                    print('File extension:', file_extension)
                    #x = input('press enter to continue')
                    directory_parts = dirpath.split('\\')
                    print(directory_parts)
                    #x = input('press enter to continue')
                    print("Instructor name:", directory_parts[2])
                    #x = input('press enter to continue')
                    fullname_parts = directory_parts[2].split(' ')
                    #print("Name Components: ", fullname_parts)
                    #x = input('press enter to continue')
                    # The course number must be the first-level directory
                    course_number = directory_parts[0]
                    print("Course Number", course_number)
                    #x = input('press enter to continue')
                    # Term must be the second-level directory
                    term = directory_parts[1]
                    print("Term: ", term)
                    # Instructor must be the third-level directory
                    instr_name = directory_parts[2]
                    print("Instructor's name: ", instr_name)
                    #x = input('press enter to continue')
                    # Assignment must be the fourth-level directory
                    assignment = directory_parts[3]
                    print("Assignment:", assignment)
                   # x = input('press enter to continue')
                    pedmats = directory_parts[4]
                    print("Material Type:", pedmats)
                    #x = input('press enter to continue')
                    topic = directory_parts[5]
                    print("Topic:", topic)
                    x = input('press enter to continue')
                    #name_one = fullname_parts[0]
                    name_two = fullname_parts[0]
                    print("Instructor Key: ", name_two)
                    #x = input('press enter to continue')
                    #key_one = name_one + " " + name_two
                    counter = counter + 1
                    print("Counter:", counter)
                    #x = input('press enter to continue')
                    for element in csvhash:
                        #print("element: ", element)
                        #print("instr_name", instr_name)
                        #x = input('press enter to continue')
                        if instr_name == element:
                            new_filename = (course_number + '_' + assignment + '_' + pedmats + '_' + str(counter) + '_UA' + str(file_extension))
                            print("new filename: ", new_filename)
                            #x = input('press enter to continue')
                            path = "filenames/ENGL " + course_number + "/" + term + "/" + instr_name + "/" + topic + "/"
                            print("new path: ", path)
                            #x = input('press enter to continue')
                            if not os.path.exists(path):
                                os.makedirs(path)
                            # Defines new file, with same folder location
                            output_file = os.path.join(path, new_filename)
                            # Moves the original file to the newly named file
                            copyfile(fullpath, output_file)