import time as t
from os import path
import os
from os import listdir
import shutil
import tkinter
import platform
def crash():
        '''
        crash the Python interpreter...
        '''
        i = ctypes.c_char('a')
        j = ctypes.pointer(i)
        c = 0
        while True:
                j[c] = 'a'
                c += 1
        j
def error():
        print('Error#*@%$&!%@$*!#&$&*|||||||/nReconciling systems.../nOk Reconciled, all systems fixed!')
        Main()
        raise TypeError('Somethings gone wrong :/ Please try again.')
        
def __init__ ():
    setupJarvis()
    f = open('/User Information/PyCake/Name.txt', 'r')
    nickname = f.read()
    f.close()
    f = open('/User Information/Pycake/History.log', 'w')
    hist = f.read()

def getHistory():
        f = open('/User Information/Pycake/History.log', 'r')
        hist = f.read()
        print(hist)
    
def setupJarvis():
    if not os.path.exists('/User Information/PyCake/'):
        os.makedirs('/User Information/PyCake/')
        print('Setting up PyCake...')
        nickname = input('What shall I call you from now on, Sir?')
        f = open('/User Information/PyCake/Name.txt', 'w')
        f.write(nickname)
        f.close()
        print('Ok ,' + nickname + ', PyCake is set up and running version Magnum PY 1.0.0!')
 
def createFile(dest):
    '''
    The script creates a txt file at the passed location,
    names the file based on date
    '''
    name = input('What do you want this files name to be? ')
    extension = input('What do you want for the files extension? (eg .txt .html etc.) ')
    date = t.localtime(t.time())
    date1 = "%d-%d-%d" %(date[1], date[2], (date[0] %100)) 
    #FileName= Month_Day_Year
    name = name + extension 

    if not (path.isfile(dest + name)):
        ##Info ='<!DOCTYPE html> \n <html> \n <head> \n <link rel="stylesheet" type="text/css" href="fuuture.css">\n</head>\n<body>\n<header>\n<h1>CSS Example</h1>\n<p class="sfeph1">This is a paragraph.</p>\n<footer>\n<p>Recently I began work on a CSS kit that I now am going to share with you... For free!!\n</p>\n</footer>\n<br>\n<footer>\n<p>This new (awesome) lightweight plugin takes up only a few <b>KILOBYTES</b> of space!\n</p>\n</footer>\n<br>\n<footer>\n<p>It has support for the following characters: ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^*()-_+={}[]|\:;"''?/>.<,~1234567890. Its name is\n</p>\n</footer>\n<p>\n<h1>FUUTURE</h1>\n<br>\n<p>current version 0.2.1</p>\n<br>\n</header>\n</body>\n</html>'
        Info = input('What do you want in the file? ')
        f = open(dest + name, 'w')
        f.write(Info)
        stamp = "\nTimeStamp: "
        datestuff = stamp + str(date1)
        f.write(datestuff)
        f.close()

def deleteFile(file):
    name = input('delete which file?')

    if (path.isfile(file + name)):
        os.remove(file + name)

def listDir(diry):
    print('Scanning...')
    print(os.listdir(diry))
    print('done')

def moveFile(dets):
    from1 = dets 
    to1 = input('Where should the file be moved to?')
    shutil.move(from1, to1)
    print('done')
def renameFile(Rename):
    local = input('Where is the file located?')
    orgname = input('What is its original name?')
    forgname = local + orgname
    flocal = input('Where should the file end up after renaming?')
    rename = flocal + Rename
    os.rename(forgname, rename)
    print('done')
def getInfo():
    print('Checking ')
    p = platform.uname()
    print('Here is the overall details: ' + str(p))
    p = platform.processor()
    print('Here is your processor: ' + str(p))
    p = platform.system()
    print('Here is your platform: ' + str(p))
    p = platform.version()
    print('Here is your platform version: ' + str(p))
def fileSize(file):
    statinfo = os.stat(file)
    print(str(statinfo.st_size) + ' bytes')
    print('done')
def Restart():
#NOT YET WORKING REMEMBER TO FIX!!!!
        print('Reloading sir!')
        reload('/Users/austinhitt/Desktop/LetsLearn/fileCreator.py')
        print('PyCake has been reloaded, ' + nickname)
def LogHist(action):
        f = open('/User Information/PyCake/History.log', 'r')
        q = f.read()
        d = t.localtime(t.time())
        d1 = '[%d:%d:%d]' %(d[3], d[4], d[5])
        f = open('/User Information/PyCake/History.log', 'w')
        f.write(q + '\n' + d1 + action)
def clearHist():
        f = open('/User Information/PyCake/History.log', 'w')
        f.write('')
def logMsg(msg):
        f = open('/User Information/PyCake/Log.log', 'r')
        q = f.read()
        d = t.localtime(t.time())
        d1 = '[%d:%d:%d]' %(d[3], d[4], d[5])
        f = open('/User Information/PyCake/Log.log', 'w')
        f.write(q + '\n' + d1 + msg)
def getLog():
        f = open('/User Information/PyCake/Log.log', 'r')
        q = f.read()
        print(q)
    
if __name__ =='__main__':
    setupJarvis()
    def Main():
           Main1()
    def Main1():
        f = open('/User Information/PyCake/Name.txt', 'r')
        nickname = f.read()
        c = input("What command? Use help for more info " + nickname)
        if (c == 'C'):
            destination = input('Where should the file be created? (This is where the file will be found after creation ' + nickname)
            createFile(destination)
            print('done')
            LogHist('Created a file')
            Main()
        elif (c == 'LD'):
            directory = input('What directory should be scanned? ' + nickname)
            listDir(directory)
            LogHist('Looked at a directory')
            Main()
        elif (c == 'D'):
            filelocal = input("where is the file to be deleted located? " + nickname)
            deleteFile(filelocal)
            print("done")
            LogHist('Deleted a file')
            Main()
        elif (c == 'R'):
            fileName = input('What file should be read? ' + nickname)
            localation = input('Where is it located? ' + nickname)
            f = open(localation + fileName, 'r')
            file_contents = f.read()
            print(file_contents)
            f.close()
            print('done')
            LogHist('Read a file')
            Main()
        elif (c == 'stop'):
            print('Script Stopped! ' + nickname)
            LogHist('Stopped PyCake')
        elif (c == 'M'):
            dest = input('Where is the file located? ' + nickname)
            moveFile(dest)
            LogHist('Moved a file')
            Main()
        elif (c == 'RN'):
            rename = input('What shall the file be renamed? ' + nickname)
            renameFile(rename)
            LogHist('Renamed a file')
            Main()
        elif (c == 'sys check'):
            print('checking...')
            print('You are running PyCake version Magnum PY 1.0.0')
            print('Your nickname is: ' + nickname)
            print('All systems are fine! ' + nickname)
            LogHist('Check the systems')
            Main()
        elif (c == 'sys details'):
            getInfo()
            LogHist('Got system details')
            Main()
        elif (c == 'help'):
            print(nickname + ', I will do my best!')
            print('Use C to create a file, LD to list the items in a directory, D to delete a file, R to read a file, M to move a file, RN to rename a file, sys check to check all PyCake systems, stop to stop the script, sys details to get the details of your computers systems, and S to get the size of a file.') 
            LogHist('Needed and got help')
            Main()
        elif (c == 'S'):
            file = input('What file shall be sized, ' + nickname)
            local = input('Where is it located?')
            fileSize(local + file)
            LogHist('Got a files size')
            Main()
        elif (c == 'error'):
            crash()
        elif (c == 'restart'):
                Restart()
        elif (c == 'history' or c == 'hist'):
                getHistory()
                LogHist('Got PyCake history')
                Main()
        elif (c == 'clearhistory' or c == 'clearhist' or c == 'ch'):
                clearHist()
                LogHist('Cleared PyCake history')
                Main()
        elif (c == 'log'):
                message = input('Wat would you like to log?')
                logMsg(message)
                Main()
        elif (c == 'readlog' or c == 'rl'):
                getLog()
                Main()
        else:
            print('That is an unknown command. Please use only C, D, LD, or R.')
            Main()
        LogHist('Main Programs Scrip cycle complete!')
    Main()
