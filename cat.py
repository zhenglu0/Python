#!/usr/bin/python

import sys

def Cat(filename):
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

  f.close()

def main():
  Cat(sys.argv[1])

if __name__ == '__main__':
  main()
