import os
import sys
from datetime import datetime

path_to_dir = sys.argv[1:]
path_to_file = path_to_dir
open_path = path_to_dir[1]

if "-d" in path_to_dir and "-f" in path_to_dir:
    path_to_file = path_to_dir[path_to_dir.index("-f"):]
    path_to_dir = path_to_dir[path_to_dir.index("-d"): path_to_dir.index("-f")]
    open_path = os.path.join(*(path_to_dir[1:] + path_to_file[1:]))  #
    # path without "-d" and "-f"

if path_to_dir[0] == "-d":
    path_to_dir = path_to_dir[1:]
    path_to_dir = os.path.join(*path_to_dir)
    os.makedirs(path_to_dir)

path_to_dir = path_to_file
if path_to_dir[0] == "-f":
    with open(open_path, "a") as made_file:
        string = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        str_num = 0
        result = True
        while result:
            str_num += 1
            made_file.write(string)
            string = input("Enter content line: ")
            string = f"\n{str_num} {string}"
            if string == f"\n{str_num} stop":
                made_file.write("\n\n")
                result = False
