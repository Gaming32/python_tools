from tkinter import *
import sys, io

class LabelFile(Label):
    ReadError = io.UnsupportedOperation('not readable')
    def __init__(self, master=None, redir_stdout=NO, cnf={}, **kw):
        Label.__init__(self, master, cnf, **kw)
        if redir_stdout: sys.stdout = self
    def read(self):
        raise self.ReadError
    def write(self, text):
        self.config(text=text)
        self['text'] += text
        sys.stderr.write(text)
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
        return
    def __iter__(self):
        raise self.ReadError

if __name__ == '__main__':
    win = Tk()
    lbl = LabelFile(win, redir_stdout=YES)
    lbl.pack(expand=YES, fill=BOTH)
    def go():
        print('Hello')
        from time import sleep
        for i in range(5, 0, -1):
            sleep(1)
            print('Time remaining', i, end='\r')
        sleep(2)
        print('OVER')
        sleep(5)
        win.quit()
    win.after(5000, go)
    win.mainloop()