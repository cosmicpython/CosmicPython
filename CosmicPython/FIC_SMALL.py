import requests
from os import getcwd
import os
import filecmp

def getfile(filename, rawlink):
    url = rawlink
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))) + os.sep
    try:
        makedir = os.mkdir(location + "Verify" + os.sep)
    except FileExistsError:
        pass
    dir = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))) + os.sep + 'Verify' + os.sep
    filedir = dir + filename + '.py'
    r = requests.get(url)
    contents = r.content
    f = open(filedir, 'w+b')
    f.write(contents)

def compare(f1, f2):
    f1f = open(f1)
    f2f = open(f2)
    f1_line = f1f.readline()
    f2_line = f2f.readline()
    while f1_line != '' or f2_line != '':
        f1_line = f1_line.rstrip()
        f2_line = f2_line.rstrip()
        if f1_line != f2_line:
            return False
        elif f1_line == f2_line:
            return True
        f1_line = f1.readline()
        f2_line = f2.readline()
    f1.close()
    f2.close()

def ForceUpdate(filedir, filename, rawlink):
    geturl = rawlink
    filepos = filedir + '.py'
    r = requests.get(geturl)
    contents = r.content
    f = open(filepos, 'w+b')
    f.write(contents)

def AutoUpdate(f1dir, rawlink, Tempfilename, f2dir, newfilename, filereplacedir):
    getfile(Tempfilename, rawlink)
    if compare(f1dir, f2dir) == True:
        ForceUpdate(filereplacedir, newfilename, rawlink)
    else:
        print('files up to date')
