#!/usr/bin/env python3
import os
import shutil
from mdmdrupaldb import FILES

#rsync -auv --relative meteo:/cygdrive/d/Services/drupal_merge .
SRC_BASEPATH = '/cygdrive/d/Services/drupal_merge'
DST_BASEPATH = './mdmdrupal/'

FILE_RSYNCLIST = 'rsync_filelist.txt'
N=0
with open(FILE_RSYNCLIST, 'w') as f:
  for file_row in FILES():
    filepath = file_row['filepath']
    f.write(filepath + '\n')
    N = N + 1
print(f'{N} files processed')
print(f'rsync -auv --progress --files-from={FILE_RSYNCLIST} meteo:{SRC_BASEPATH} {DST_BASEPATH}')

COPY_FILES = False
if COPY_FILES:
  for file_row in FILES():
    filepath = file_row['filepath']
    dst_pathname = CONTENT_BASEPATH + 'repo/' + os.path.dirname(filepath)
    src_pathname = FILE_BASEURL + filepath
    print(f'Copy:\n SRC: {src_pathname}\n  DST: {dst_pathname}')
    print(f'  Creating content in {dst_pathname}')
    os.makedirs(dst_pathname, exist_ok = True)
    try:
      shutil.copy2(src_pathname, dst_pathname, follow_symlinks=True)
      print('  OK!')
    except:
      print('  FAILED!')
