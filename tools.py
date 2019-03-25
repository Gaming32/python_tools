"A module with tools to help you program with python"

from time import clock
applicationruntime = clock
del clock

def fix_none(var, desired_type): 
    "Returns var if var isn't None, otherwise it returns desired_type()"
    return (desired_type() if var == None else desired_type(var))

def str_split_len(string, substrLength):
    "Returns a list of strings of the length specified in substrLength"
    words = []
    for i in range((len(string) // substrLength) + 1):
        i *= substrLength
        words.append(substr(string, i, substrLength) if len(string) - i >= substrLength else substr(string, i, len(string) - i))
    if '' in words: words.remove('')
    return words

def substr(string, start, length):
    "Provides a classic substring function"
    return string[start:start + length]

import os
import sys
def impfile(path, name=None):
    path = path.split(os.sep)
    if not name:
        name = path[-1]
    sys.path.append(os.sep.join(path[:-1]))
    exec('import %s as %s' % (path[-1], name))
    sys.path[-1] = []

def runfile(file, *args):
    if sys.platform[:3] == 'win': os.startfile(os.path.abspath(file))
    else:
        if os.fork() == 0: os.execl(file, *args)

if __name__ == "__main__":
    var = {1:10,2:20,3:30}
    var = fix_none(var, dict)
    print(repr(var))