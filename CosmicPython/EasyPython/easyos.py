'''
NOTES

https://docs.python.org/3.1/library/os.html

'''

import os

#######################################
'''
Example    osinfo('osname')     
this will return Linux if you are on a Linux operating system

data set can be:
) osall - gives all data provided with no sorting same as os.uname()
) osname - name of the running operating system, for example Linux
) nodename - the kind of machin you are running so to say
             for example 'vm' or virtual machine
) version - the version of the operating system you are running
) release - when the version of your operating system was released
) ostype - for example x86_64
'''
def osinfo(dataset):
    uname = os.uname()
    osdata = dict(
            osall = os.uname(),
            osname = uname[0],
            nodename = uname[1],
            version = uname[2],
            release = uname[3],
            ostype = uname[4]
    )
    return osdata[dataset]
######################################
'''
Example

ospdata can be:
ospall - gives all data provided with no sorting same as os.stat(path)
mode - 
ino - 
dev - 
nlink - 
uid - 
gid - 
size - 
atime - 
mtime - 
ctime - 

With Linux it can also be:
blocks - 
blksize - 
rdev - 
flags - 

With MacOS it can be:
rsize - 
creator - 
osptype - 
'''
def ospstat(path, dataset):
    ospath = os.stat(path)
    ospsdata = dict(
            ospall = ospath,
            mode = ospath[0],
            ino = ospath[1],
            dev = ospath[2],
            nlink = ospath[3],
            uid = ospath[4],
            gid = ospath[5],
            size = ospath[6],
            atime = ospath[7],
            mtime = ospath[8],
            ctime = ospath[9],
            blocks = ospath[10],
            rsize = ospath[10],
            blksize = ospath[11],
            creator = ospath[11],
            rdev = ospath[12],
            osptype = ospath[12],
            flags = ospath[13]
    )
    return ospsdata[dataset]
######################################
