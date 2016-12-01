#!/usr/bin/env python

import os
import sys
import subprocess

# Usage
# mgs.py ==> show all girl's videos
# mgs.py girlname ==> show all videos about this girl
# mgs.py girlname video ==> use vlc to play the video

if len(sys.argv) > 1:
    find_path = '/tmp/xxoo/' + sys.argv[1]
else:
    find_path = '/tmp/xxoo'

for dirpath, dirnames, filenames in os.walk(find_path):
    for filename in filenames:
        video_file_suffix = filename[-4:]
        # filter video file
        if video_file_suffix == '.mp4' or video_file_suffix == '.wmv' or video_file_suffix == '.m4v':
            # find out file full path and depth
            full_filename = dirpath + '/' + filename
            dirsplit = full_filename.split('/');
            dirdepth = len(dirsplit) - 3
            # print format filename[depth]
            if dirdepth == 1:
                print filename + '[' + str(dirdepth) + ']'
            elif dirdepth == 2:
                print filename + '[' + str(dirdepth) + ']'
            else:
                print filename + '[' + str(dirdepth) + ']'

            # compare the file name without the suffix
            if len(sys.argv) > 2 and filename[:-4] == sys.argv[2]:
                subprocess.Popen(['/usr/bin/vlc', full_filename])

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
