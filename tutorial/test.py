#!/usr/bin/python

import sys
import os
import commands

def Cat(filename):
  try:
    f = open(filename, 'rU')
    #1. read each line at a time
    #for line in f:
    #  print line,
    
    #2. read line as a list
    #lines = f.readlines()
    #print lines

    #3. read text as string
    text = f.read()
    print text
    file.close()
  except IOError:
    print filename, "could not be opened."


def List(dir):
  cmd = 'ls -l ' + dir
  print 'about to do this:', cmd
  (status, output) = commands.getstatusoutput(cmd)
  if status:
    print sys.stderr, 'there was an error:' , output
    sys.exit(1)
  print output
  # filenames = os.listdir(dir)
  # for filename in filenames:
  #   path = os.path.join(dir, filename)
  #   print path
  #   print os.path.abspath(path)

def main():
  Cat(sys.argv[1])
  List(sys.argv[1])

if __name__ == '__main__':
  main()
