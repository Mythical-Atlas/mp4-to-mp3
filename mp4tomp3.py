# mp4 to mp3 converter
# written by Ben Correll

import os
import sys
from moviepy.editor import *

def Convert_MP4(src):
    x = list(src)
    x.pop()
    dst = "".join(x)
    dst += "3"

    try:
        AudioFileClip(src).write_audiofile(dst)
    except:
        print("Error converting " + src + " to " + dst)
        
        sys.exit(1)

    print("Successfully converted " + src + " to " + dst)

if(len(sys.argv) != 2):
    print("Usage:")
    print("  python mp4tomp3.py source_file")
    print("  python mp4tomp3.py source_directory")
    
    sys.exit(0)

src = os.path.realpath(sys.argv[1])

convert_dir = False

if(os.path.isfile(src)):
    if(not src.endswith(".mp4")):
        print("Source file must be an MP4")
        
        sys.exit(1)
else:
    if(os.path.isdir(src)):
        convert_dir = True
    else:
        print("Could not find source file or directory specified")
        
        sys.exit(1)

if(not convert_dir):
    Convert_MP4(src)
else:
    files = os.listdir(src)
    
    for file in files:
        file_path = os.path.realpath(src + "\\" + file)
    
        if(os.path.isfile(file_path) and file_path.endswith(".mp4")):
            Convert_MP4(file_path)