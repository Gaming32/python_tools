import os

def shortest(*paths):
    res = []
    for path in paths:
        res.append(len(os.path.normpath(path).split(os.path.sep)))
    return paths[res.index(min(res))]

def bestrel(path, *starts):
    bests = []
    for start in starts:
        testpath = os.path.relpath(path, start)
        if not '..' in testpath:
            bests.append(testpath)
    if not bests:
        for start in starts:
            bests.append(os.path.relpath(path, start))
    return shortest(*bests)

def deldir(path):
    for sub in os.listdir(path):
        sub = os.path.join(path, sub)
        if os.path.isdir(sub):
            deldir(sub)
        elif os.path.isfile(sub):
            os.remove(sub)
    os.rmdir(path)

if __name__ == '__main__':
    deldir(r"C:\Users\josia\MEGA\Projects\Programming Languages\Python\tkGame\cache\run\7f5e569dcd47aa8569336ffbb15b9664")