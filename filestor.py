def storereprlist(file, *items):
    for item in items:
        file.write(repr(item))
        file.write('\n')
def readreprlist(file):
    for line in file:
        line = line[:-1]
        yield eval(line)

if __name__ == '__main__':
    fname = 'reprlist'
    import os
    if os.path.exists(fname):
        file = open(fname, 'r+')
    else:
        file = open(fname, 'w+')
    import pprint
    pprint.pprint(list(readreprlist(file)))
    mylist = ['Some Text', 12345, [0, 1, 2], {'a':10, 'b':20, 'c':30}]
    storereprlist(file, *mylist)