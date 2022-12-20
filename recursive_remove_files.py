#! /usr/bin/python
# -*- coding: utf-8 -*-

import os

cwd = os.getcwd()
print(cwd)

# --------------------------- User input
dir1 = "C:\\Users\\mat\\Documents\\3_"

files_to_delete = ['.pyc']

notepad = "/c/Program\ Files\ \(x86\)/Notepad++/notepad++.exe "
# --------------------------- End User input

for root, dirs, files in os.walk(dir1):
    for file in files:
        if file.endswith(".pyc"):
            f = os.path.join(root, file)
            print(f)
            # os.remove(f)
