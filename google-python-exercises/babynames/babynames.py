#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  try:
    f = open(filename, 'rU')
    # read text as a string
    text = f.read()
    f.close()
    result = []
    m = re.search(r'<h[^<]*>[^0-9]*(\d+)</h\d>',text)
    if m:
      year = m.group(1)
      result.append(year)
    #print result
    rank_dict = {}
    tuples = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>',text)
    # print tuples
    for t in tuples:
      if t[1] in rank_dict:
        # print t[1], "already in dictionary, will choose a larger value between" , t[0] , rank_dict[t[1]]
        rank_dict[t[1]] = t[0] if t[0] > rank_dict[t[1]] else rank_dict[t[1]]
      else:
        rank_dict[t[1]] = t[0]
      if t[2] in rank_dict:
        # print t[2], "already in dictionary, will choose a larger value between" , t[0] , rank_dict[t[2]]
        rank_dict[t[2]] = t[0] if t[0] > rank_dict[t[2]] else rank_dict[t[2]]
      else:
        rank_dict[t[2]] = t[0]
    keys = sorted(rank_dict.keys())
    for key in keys:
      result.append(key + ' ' + rank_dict[key])
      #print result
    return result
  except IOError:
    print filename, "could not be opened."

def print_to_file(results):
  file = open('result.txt', 'w')
  for result in results:
    file.write('\n'.join(result))
  file.close()

def print_to_screen(results):
  for result in results:
    print '\n'.join(result)

def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file  
  results = []
  for arg in args:
    result = extract_names(arg)
    results.append(result)

  if summary:
    print_to_file(results)
  else:
    print_to_screen(results)

if __name__ == '__main__':
  main()
