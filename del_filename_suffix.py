# -*- coding:utf-8 -*-

import os


def isSuffix(suffixs, filename):
    flag = true;
    for suffix in suffixs:
        if not(suffix in filename):
            flag = false
    return flag

def delFilenameSuffix(dir):
    fileList = []
    fileNames = os.listdir(dir)
    
    if (len(fileNames) > 0):
        for fn in fileNames:
            splittext = os.path.splitext(fn)
            print("%s, %s, %s" % (fn, splittext[0], splittext[1]))
            os.rename(os.path.join(dir,fn),os.path.join(dir,splittext[0]))
            
delFilenameSuffix(os.getcwd());

            