#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands
import zipfile

"""Copy Special exercise
   Copy or zip all file which has __(\w+)__ in the file name,
   and remove __ when doing the copy
"""

# +++your code here+++
# Write functions and modify main() to call them
def find_special_file(dir):
  result = []
  names = os.listdir(dir)
  # print names
  for name in names:
    match = re.search(r'__\w+__', name)
    if match:
      result.append(os.path.join(dir, name))
  # print result
  return result

def copy_files(paths, to_dir):
  if not os.path.exists(dst):
    print "mkdir ", dst
    os.mkdir(dst)

  for file in paths:
    shutil.copy(file, dst)

def zip_files(paths, to_zip):
  # 1 using zip module
  # zip_path = os.path.join('.', to_zip)
  # zipf = zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED)
  # for path in paths:
  #   zipf.write(path)
  # 2 use commands.getstatusoutput
  cmd = 'zip -j ' + to_zip + ' ' + ' '.join(paths)
  print "Command to run:", cmd   ## good to debug cmd before actually running it
  (status, output) = commands.getstatusoutput(cmd)
  if status:    ## Error case, print the command's output to stderr and exit
    sys.stderr.write(output)
    # sys.exit(status)
  print output

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args and args[0] == '--todir':
    todir = args[1]
    del args[0:2]
  # print 'todir = ', todir

  tozip = ''
  if args and args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]
  # print 'tozip = ', tozip

  src_dirs = args

  # print "src dirs" , src_dirs

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  special_file_paths = []
  for src_dir in src_dirs:
    special_file_paths += find_special_file(src_dir)

  if tozip:
    zip_files(special_file_paths, tozip)
  elif todir:
    copy_files(special_file_paths, todir)

if __name__ == "__main__":
  main()
