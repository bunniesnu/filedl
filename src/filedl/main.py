from requests import get
from os import getcwd
from os import makedirs
from os.path import exists
from sys import argv
from sys import exit

link = ""
output = getcwd()
path = ""

def help():
    print(
"""Filedl v1.0.0""")

skip = False

for i in range(len(argv)):
    if skip == 0:
        if argv[i] == "-h" or argv[i] == "--help":
            help()
            exit(0)
        elif argv[i] == "-o" or argv[i] == "--output":
            try:
                output = argv[i+1]
                skip = True
            except:
                print("No output path given.")
                exit(1)
        elif argv[i] == "-f" or argv[i] == "--filename":
            try:
                path = argv[i+1]
                skip = True
            except:
                print("No output file name given.")
                exit(1)
        else:
            link = argv[i]
    else:
        skip = 0

if path == "":
    path = link.split("/")[-1]

# Prettier directory
if not output[0] in "./":
    output = "./" + output
if output[:2] == "./":
    output = getcwd() + "/" + output[2:]
if output[-1] != "/":
    output = output + "/"

# Get full path
fullpath = output + path

# Make directory if not exists
if not exists(output):
    makedirs(output)

# Check if file already exists
if exists(fullpath):
    print("File already exists")
    exit(1)

try:
    img_data = get(link).content
except:
    print("Try with valid url.")
    exit(1)

try:
    with open(fullpath, 'wb') as handler:
        handler.write(img_data)
except:
    print(f"Output path is not valid: {fullpath}")
    exit(1)

print(f"Saving to {fullpath}")
exit(0)