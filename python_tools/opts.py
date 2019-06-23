import sys

def _isdopop(dopop, argv):
    if dopop:
        return (lambda i, argv=argv: argv.pop(i))
    else:
        return (lambda i, argv=argv: argv[i])

def getallopts(argv=None, dopop=True):
    if argv is None:
        argv = sys.argv[1:]
    get = _isdopop(dopop, argv)
    rest = []
    i = 0
    while True:
        value = get(i)
        if value[0] == '-':
            yield value, get(i)
        else:
            rest.append(value)
        if not len(argv):
            break

if __name__ == '__main__':
    for item in getallopts():
        print(item)