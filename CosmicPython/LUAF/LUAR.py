import os
import time
from cryptography.fernet import Fernet
from LUAFK import key

class register:
    global f
    f = Fernet(key)

    def reguser(username, password):
        user = username
        passw = password
        uencode = user.encode()
        pencode = passw.encode()
        #encrypts the username and password
        encryptuname = f.encrypt(uencode)
        encryptupass = f.encrypt(pencode) 
        encryptn = str(encryptuname)
        encryptp = str(encryptupass)
        namelen = len(encryptn) - 1
        passlen = len(encryptp) - 1
        #removed the b' at the beginning of the encrypted username
        #and password and removes the last '
        rname = encryptn[2:namelen]
        rpass = encryptp[2:passlen]
        try:
            #gets the current path and makes a folder named LA
            path = str(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))) + '/ELA'
            os.mkdir(path)
        except FileExistsError:
            print('working...')
        if os.path.isfile(path + '/' + username + '.txt') == False:
            if len(username) <= 24 and len(password) <= 40 and len(username) >=3 and len(password) >=1:
            #checks if username and password do not exceed the stated maximum and minimum
                IllegalChars = ['$', '@', '/', '[', ']', '{', '}', '<', '>', '=', '+', '?', '#', '%', '^', '&', '*', '(', ')', '|', ';', ':', ',', '~', '`', '\\', "\'", '\"', '.', ' ']
                if any(x in username for x in IllegalChars):
                    #checks that the username does not have any illegal characters
                    print('Your username cannot contain Illegal characters')
                    print('it can contain ! though')
                else:
                    #if everything is true or passes then it will create the account
                    arfile = open(os.path.join(path, str(username) + '.txt'), 'a')
                    wrfile = open(os.path.join(path, str(username) + '.txt'), 'w')
                    wrfile.write(rname)
                    arfile.write('\n' + rpass)
                    wrfile.close()
                    arfile.close()
                    time.sleep(3)
            else:
                print('your username(3-24) or password(1-40) is too long or too short')
        else:
            print('Either your username exists or it is a system error')
