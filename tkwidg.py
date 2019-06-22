from tkinter import *
import sys, io

class LabelFile(Label):
    ReadError = io.UnsupportedOperation('not readable')
    def __init__(self, master=None, redir_stdout=NO, buffered=True, cnf={}, **kw):
        if not 'anchor' in cnf and not 'anchor' in kw: kw['anchor'] = NW
        if not 'font'   in cnf and not 'font'   in kw: kw['font']   = ('courier', 10, NORMAL)
        Label.__init__(self, master, cnf, **kw)
        if redir_stdout: sys.stdout = self
        self.buffered = buffered
    def read(self):
        raise self.ReadError
    def write(self, text):
        #self.config(text=text)
        self['text'] += text
        if not self.buffered: self.flush()
        #sys.stderr.write(text)
        return len(text)
    def readline(self):
        raise self.ReadError
    def writelines(self, lines):
        self.write(lines[-1])
    def readlines(self):
        raise self.ReadError
    def readable(self):
        return True
    def writable(self):
        return False
    def flush(self):
        try: self.update()
        except TclError: pass
    def __iter__(self):
        raise self.ReadError

def hidewin(win, hidden):
    "Hides or shows win based on the value of hidden"
    win.overridedirect(hidden)
    if hidden: win.iconify()
    else: win.deiconify()

if __name__ == '__main__':
    win = Tk()
    lbl = LabelFile(win, redir_stdout=YES, buffered=False)
    lbl.pack(expand=YES, fill=BOTH)
    def go():
        print('Hello')
        from time import sleep
        for i in range(5, 0, -1):
            sleep(1)
            print('Time remaining', i, end='\r')
        sleep(2)
        print('\nOVER')
        sleep(5)
        win.quit()
    win.after(5000, go)
    win.mainloop()