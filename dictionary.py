import os, sys
import random
_defenc = sys.getdefaultencoding()

_getwordsfile_dloadloc = 'http://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words'
def getwordsfile(dodownload=False, downloadloc=_getwordsfile_dloadloc, downloadout=None):
    dictfile = ''
    locs = [
        '/usr/share/dict/words'
    ]
    for loc in locs:
        if os.path.isfile(loc):
            dictfile = loc
            break
    else:
        if dodownload == 1:
            if downloadout is None: downloadout = locs[0]
            import urllib.request as request, shutil
            fin = request.urlopen(downloadloc)
            outdir = '/'.join(downloadout.split('/')[:-1])
            if not os.path.exists(outdir): os.makedirs(outdir)
            fout = open(downloadout, 'wb')
            shutil.copyfileobj(fin, fout)
            fout.close()
            dictfile = downloadout
        elif dodownload == 0:
            raise FileNotFoundError
    return dictfile
wordsfile = getwordsfile(2)
openwordsfile = lambda wordsfile=wordsfile: open(wordsfile)

def getwordslist(wordsfile_=wordsfile):
    if wordsfile_ == wordsfile and openedwordsfile:
        openedwordsfile_ = openedwordsfile
    else:
        openedwordsfile_ = openwordsfile(wordsfile_)
    res = []
    for line in openedwordsfile_:
        res.append(line.strip())
    return res
try:
    openedwordsfile = openwordsfile()
    wordslist = getwordslist()
except OSError:
    openedwordsfile = None
    wordslist = []

# lowerwordslist = lambda: (x.lower() for x in wordslist)

def scramble(word, random_=None):
    word = list(word)
    random.shuffle(word, random_)
    return ''.join(word)

def unscramble(word, lowercaps=True):
    if lowercaps: word = word.lower()
    word = list(word)
    worddef = word[:]
    if lowercaps: mywordslist = [x.lower() for x in wordslist]
    else: mywordslist = wordslist
    for testword in mywordslist:
        for (i, char) in enumerate(testword):
            if char in word:
                word.pop(word.index(char))
            else: break
            if i == len(testword) - 1 and word: break
        else:
            yield testword
        word = worddef[:]


if __name__ == '__main__':
    wordsfile = getwordsfile(True)
    openedwordsfile = openwordsfile()
    wordslist = getwordslist()
    get = lambda name: sys.argv[sys.argv.index(name) + 1]
    done = False
    if   '-s' in sys.argv:
        done = True
        print('Scrambled:')
        print('   ', scramble(get('-s')))
    elif '--scramble' in sys.argv:
        done = True
        print('Scrambled:')
        print('   ', scramble(get('--scramble')))
    if   '-u' in sys.argv:
        done = True
        print('Unscrambled:')
        for result in unscramble(get('-u'), not ('-caps' in sys.argv or '--capitalization' in sys.argv)):
            print('   ', result)
    elif '--unscramble' in sys.argv:
        done = True
        print('Unscrambled:')
        for result in unscramble(get('--unscramble'), not ('-caps' in sys.argv or '--capitalization' in sys.argv)):
            print('   ', result)
    if not done or '-h' in sys.argv or '--help' in sys.argv:
        print('Usage:', sys.executable, __file__, '[-h|--help]', '[-caps|--capitalization]',
        '[-s|--scramble <word>]', '[-u|--unscramble <scrambled_word>]')
    # import pprint
    # pprint.pprint(list(unscramble(scramble('aloha'))))