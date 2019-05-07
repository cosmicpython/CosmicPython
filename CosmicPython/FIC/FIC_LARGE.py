import requests
from os import getcwd
import os
import filecmp

global tf
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
    tf = open(filedir, 'w+b')
    tf.write(contents)

def compare(f1, f2):
    if filecmp.cmp(f1, f2, shallow=True) == True:
        tf.close()
        return True
    elif filecmp.cmp(f1, f2, shallow=True) == False:
        tf.close()
        return False

def ForceUpdate(filedir, filename, rawlink):
    geturl = rawlink
    filepos = filedir + filename + '.py'
    r = requests.get(geturl)
    contents = r.content
    ttf = open(filepos, 'w+b')
    ttf.write(contents)

def AutoUpdate(f1dir, rawlink, Tempfilename, f2dir, newfilename, filereplacedir):
    getfile(Tempfilename, rawlink)
    if compare(f1dir, f2dir) == True:
        ForceUpdate(filereplacedir, newfilename, rawlink)
    else:
        print('files up to date')
