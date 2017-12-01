#!/usr/bin/python

import sys
import os
import commands
import array

### Python test read file
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

### Python execute command
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

### Python test golbal varible
### https://www.tutorialspoint.com/python
Money = 2000
def AddMoney():
   # Uncomment the following line to fix the code:
   global Money
   Money = Money + 1

def main():
  #Cat(sys.argv[1])
  #List(sys.argv[1])
  print Money
  AddMoney()
  print Money

  # https://stackoverflow.com/questions/16887493/write-a-binary-integer-or-string-to-a-file-in-python
  bin_array = array.array('B')

  bin_array.append(int('011',2))
  bin_array.append(int('010',2))
  bin_array.append(int('110',2))

  f = file('binary.mydata','wb')
  bin_array.tofile(f)
  f.close()

  filename = raw_input("Enter your filename: ");
  print "Received filename is : ", filename

  # Open a file
  f = open(filename, "wb")
  f.write("Python is a great language.\nYeah its great!!\n 12345\n");

  # Open a file
  f = open(filename, "r+")
  str = f.read(10);
  print "Read String is : ", str

  # Check current position
  position = f.tell();
  print "Current file position : ", position

  # Reposition pointer at the beginning once again
  position = f.seek(0, 0);
  str = f.read(2);
  print "Again read String is : ", str
  # Close opend file
  f.close()

  # Rename a file from test1.txt to test2.txt
  os.rename( filename, "test2.txt" )

  # Delete file test2.txt
  os.remove(os.path.join('.',"test2.txt"))

if __name__ == '__main__':
  main()
