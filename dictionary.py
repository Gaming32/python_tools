import os, sys
import random

from collections import OrderedDict
_getwordsfile_dloadloc = 'http://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words'
_init_filelocs = [
    '/usr/share/dict/words'
]
_init_defaults = OrderedDict(dodownload=False, downloadloc=_getwordsfile_dloadloc, downloadout=None, filelocs=_init_filelocs)
def init(dodownload=2, downloadloc=_getwordsfile_dloadloc, downloadout=None, filelocs=_init_filelocs):
    global wordsfile, openwordsfile, openedwordsfile, wordslist
    global getwordsfile, getwordslist

    _defenc = sys.getdefaultencoding()
    _getwordsfile_dloadloc = 'http://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words'
    def getwordsfile(dodownload=False, downloadloc=_getwordsfile_dloadloc, downloadout=None):
        dictfile = ''
        
        for loc in filelocs:
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
    wordsfile = getwordsfile(dodownload)
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
init.__defaults__ = tuple(_init_defaults.values())
import inspect
def preinit(*args, **kwargs):
    argnames = inspect.getfullargspec(init)[0]
    for (i, val) in enumerate(args):
        _init_defaults[argnames[i]] = val
    _init_defaults.update(kwargs)
    init.__defaults__ = tuple(_init_defaults.values())

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
    visited = set()
    for testword in mywordslist:
        if testword in visited: continue
        for (i, char) in enumerate(testword):
            if char in word:
                word.pop(word.index(char))
            else: break
            if i == len(testword) - 1 and word: break
        else:
            yield testword
            visited.add(testword)
        word = worddef[:]

def makewingui():
    form = Form()
    form.SuspendLayout()
    stxt = TextBox()
    utxt = TextBox()
    sbtn = Button()
    ubtn = Button()

    #
    # stxt
    #
    stxt.Location = Point(12, 8)
    stxt.Name = 'stxt'
    stxt.Size = Size(319, 20)
    stxt.TabIndex = 0
    #
    # utxt
    #
    utxt.Location = Point(12, 34)
    utxt.Name = 'utxt'
    utxt.Size = Size(319, 20)
    utxt.TabIndex = 2
    #
    # sbtn
    #
    sbtn.Anchor = AnchorStyles.Top | AnchorStyles.Right
    sbtn.Location = Point(337, 6)
    sbtn.Name = 'sbtn'
    sbtn.Size = Size(75, 23)
    sbtn.TabIndex = 1
    sbtn.Text = 'Scramble'
    sbtn.UseVisualStyleBackColor = True
    def sres(sender, e):
        stxt.Text = scramble(stxt.Text)
    sbtn.Click += EventHandler(sres)
    ubtn.MouseEnter += EventHandler(sres)
    #
    # ubtn
    #
    ubtn.Anchor = AnchorStyles.Top | AnchorStyles.Right
    ubtn.Location = Point(337, 32)
    ubtn.Name = 'ubtn'
    ubtn.Size = Size(75, 23)
    ubtn.TabIndex = 3
    ubtn.Text = 'Unscramble'
    ubtn.UseVisualStyleBackColor = True
    def ures(sender, e):
        utxt.Text = '/'.join(unscramble(utxt.Text))
    ubtn.Click += EventHandler(ures)
    ubtn.MouseEnter += EventHandler(ures)
    #
    # form
    #
    form.AutoScaleDimensions = SizeF(6.0, 13.0)
    form.AutoScaleMode = AutoScaleMode.Font
    form.ClientSize = Size(424, 61)
    form.Controls.Add(stxt)
    form.Controls.Add(utxt)
    form.Controls.Add(sbtn)
    form.Controls.Add(ubtn)
    form.FormBorderStyle = FormBorderStyle.Fixed3D
    form.Name = 'form'
    form.Text = os.path.basename(__file__)
    form.ResumeLayout(False)
    form.PerformLayout()

    Application.EnableVisualStyles()
    Application.Run(form)

if __name__ == '__main__':
    # wordsfile = getwordsfile(True)
    # openedwordsfile = openwordsfile()
    # wordslist = getwordslist()
    preinit(True)
    init()
    get = lambda name: sys.argv[sys.argv.index(name) + 1]
    if '--gui' in sys.argv:
        import clr
        clr.AddReference('System')
        from System import *
        clr.AddReference('System.Drawing')
        from System.Drawing import *
        clr.AddReference('System.Windows.Forms')
        from System.Windows.Forms import *
        makewingui()
        sys.exit()
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
        for result in unscramble(get('-u'), not ('--caps' in sys.argv or '--capitalization' in sys.argv)):
            print('   ', result)
    elif '--unscramble' in sys.argv:
        done = True
        print('Unscrambled:')
        for result in unscramble(get('--unscramble'), not ('--caps' in sys.argv or '--capitalization' in sys.argv)):
            print('   ', result)
    if not done or '-h' in sys.argv or '--help' in sys.argv:
        print('Usage:', sys.executable, __file__, '[-h|--help]', '[--gui]', '[--caps|--capitalization]',
        '[-s|--scramble <word>]', '[-u|--unscramble <scrambled_word>]')
    # import pprint
    # pprint.pprint(list(unscramble(scramble('aloha'))))