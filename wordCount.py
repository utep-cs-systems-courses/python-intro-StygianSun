#! /usr/bin/env python 3

import sys        # command line arguments
import re         # regular expression tools
import os         # checking if file exists
import subprocess # executing program

#set input and output files

if len(sys.argv) is not 3:
    print("Correct usage: wordCount.py <input text file> <output file>")
    exit()

input_file = sys.argv[1]
output_file = sys.argv[2]

text = open(input_file, 'r')
word_dict = dict()

if not os.path.exists(input_file):
    print("No input file with that name could be found")
    exit()

if not os.path.exists(output_file):
    print("No output file with that name could be found")
    exit()

for line in text:
    line = line.strip()
    line = line.lower()
    line = re.sub(r'[^\w\s]',' ',line)
    words = line.split(" ")

    for word in words:
        if word is not "":
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1

out_text = open(output_file, 'w')

for key in sorted(word_dict.items()):
    out_text.write(str(key[0]) + ' ' + str(key[1]) + '\n')

text.close()
out_text.close()
