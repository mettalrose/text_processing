#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import re
import glob
import os
import codecs

semesters = {'1': 'Spring', '2': 'Summer', '3': 'Fall'}
output_dir = 'output'


def splitall(path):
    allparts = []
    while 1:
        parts = os.path.split(path)
        if parts[0] == path:
            allparts.insert(0, parts[0])
            break
        elif parts[1] == path:
            allparts.insert(0, parts[1])
            break
        else:
            path = parts[0]
            allparts.insert(0, parts[1])
    return allparts

if __name__ == '__main__':
    if len(sys.argv) > 1:
        for argument in sys.argv[1:]:
            for file in glob.iglob(argument):
                if not os.path.isfile(file):
                    sys.exit('No file found at', file, '. Please try again.')
                with open(file, 'r') as f:
                    original_directory = os.path.dirname(file)
                    original_filename = os.path.basename(file)
                    filename_base, file_extension = os.path.splitext(
                        original_filename)
                    print('Full path:', file)
                    print("Original path: ", original_directory)
                    print("Original filename: ", filename_base)
                    print('File extension:', file_extension)
                    filename_parts = filename_base.split('_')
                    print("Filename parts: ", filename_parts)
                    country = filename_parts[2]
                    print("country:", country)
                    year = filename_parts[3]
                    print("year:", year)
                    gender = filename_parts[4]
                    print("gender:", gender)
                    ID = filename_parts[5]
                    print("ID:", ID)
                    directory_parts = splitall(original_directory)
                    print(directory_parts)
                    # The assignment must be the first-level directory
                    assignment = directory_parts[0]
                    print("Assignment:", assignment)
                    # Draft must be the second-level directory
                    draft = directory_parts[1]
                    draft = re.sub('D', '', draft)
                    print("Draft: ", draft)
                    
                    output_file_name = ('106i_' + '_' + assignment + '_' + draft + '_' + country + '_' + year + '_' + gender + '_' + ID + '_PRD.txt')
                    print("new file name:", output_file_name)
                    output_directory = os.path.join(output_dir, original_directory)
                    if not os.path.exists(output_directory):
                        os.makedirs(output_directory)
                    output_file_location = os.path.join(output_directory, output_file_name)
                    # for each line in this file
                    for line in f:
                        # write our text in the file
                        if (line[0:12] == '<Assignment:'):
                            text = '<Assignment: ' + assignment + '>'
                            print(text, file=open(output_file_location, "a"))
                        elif (line[0:7] == '<Draft:'):
                            text = '<Draft: ' + draft + '>'
                            print(text, file=open(output_file_location, "a"))
                        elif (line[0:14] == '<Term writing:'):
                            print ("current line:", line)
                            # x = input ('press enter to continue')
                            split_line = line.split(" ")
                            print ("split line: ", split_line)
                            # x = input ('press enter to continue')
                            semester_writing = split_line[2]
                            year_writing = split_line[3]
                            year_writing = re.sub('>', '', year_writing)
                            print ("year writing: ", year_writing)
                            # x = input ('press enter to continue')
                            text = '<Year writing: ' + year_writing + '>' 
                            print(text, file=open(output_file_location, "a"))
                            text= '<Semester writing: ' + semester_writing + '>'
                            print(text, file=open(output_file_location, "a"))
                        elif (line[0:15] == '<TOEFL-writing:'):
                            text = line[:-1] 
                            print(text, file=open(output_file_location, "a"))
                            text = "<End Header>"
                            print(text, file=open(output_file_location, "a"))
                        else:
                            if line[0:9] != '<Section:':
                                text = line[:-1] 
                                print(text, file=open(output_file_location, "a"))
