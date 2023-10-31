import os
import sys
def pythvers():
    print(sys.version)
def createdir(name):
    os.mkdir(name)
def listf():
    items=os.listdir('../')
    for item in items:
        print(item)