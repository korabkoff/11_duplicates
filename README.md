# Anti-Duplicator


This console script returns duplicates of files if their names and size are equal.

# How to run

script require python3.5
Example of script launch on Linux, Python 3.5:

```#!bash
$ python duplicates.py <directory>
# possibly requires call of python3 executive instead of just python

# output example
$ python duplicates.py /Users/John/Documents

Documents/September/Poland.pdf
Documents/October/Referenses/Poland.pdf
Documents/October/Airbnb.pdf
Documents/October/.DS_Store

$ python duplicates.py -h

usage: duplicates.py [-h] filepath

Show duplicates of files in given folder and subfolders

positional arguments:
   filepath    File path to folder

optional arguments:
  -h, --help  show this help message and exit

```


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
