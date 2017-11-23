#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib
import time
from multiprocessing import Pool

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""
protocal = 'http://'

def file_download(url_filepath):
  try:
    print 'Download', url_filepath[0], 'as', url_filepath[1]
    ufile = urllib.urlretrieve(url_filepath[0], url_filepath[1])
  except Exception as e:
    print e

def find_suffix_pattern(url):
  # print url
  match = re.search(r'-(\w\w\w\w).jpg', url)
  #print match.group(1)
  return match.group(1)

def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  hostname = filename[filename.index('_')+1:]
  # print hostname
  try:
    ## Either of these two lines could throw an IOError, say
    ## if the file does not exist or the read() encounters a low level error.
    f = open(filename, 'rU')
    text = f.read()
    f.close()
    match = re.findall(r'GET (/edu/\S+.jpg) ', text)
    urls = sorted(set(match), key = find_suffix_pattern)
    complete_urls = [protocal+hostname+url for url in urls]
    return complete_urls
  except IOError:
    ## Control jumps directly to here if any of the above lines throws IOError.
    sys.stderr.write('problem reading:' + filename)

  

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++
  if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)
  
  url_filepath = []
  filenames = []
  
  try:
    suffix = 0
    for url in img_urls:
      filename = 'img'+str(suffix)
      suffix += 1
      filepath = os.path.join(dest_dir, filename)
      filenames.append(filename)
      url_filepath.append((url, filepath))
  except IOError:
    print 'problem reading url:', url

  # Use multithreading to increase download speed

  print url_filepath

  # https://stackoverflow.com/questions/31784484/how-to-parallelized-file-downloads
  # https://docs.python.org/2/library/multiprocessing.html
  #Pool(20).map(file_download, url_filepath)
  pool = Pool(20)
  pool.imap_unordered(file_download, url_filepath)
  pool.close()
  pool.join()

  # create the index.html file to diaplay the image
  f = open(os.path.join(dest_dir,'index.html'), 'w')
  html = '<html><body>\n'
  for filename in filenames:
    html += '<img src="' + filename + '">'
  html += '\n</html></body>\n'
  f.write(html)
  
def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
