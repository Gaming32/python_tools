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