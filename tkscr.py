#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@ author: magic
"""
import Tkinter


def button():
    root = Tkinter.Tk()
    quit = Tkinter.Button(root, text='Hello Magic!', command=root.quit)
    quit.pack()
    Tkinter.mainloop()


def th():
    root = Tkinter.Tk()
    hello = Tkinter.Label(root, text="Hello Magic")
    hello.pack()

    quit = Tkinter.Button(root, text='QUIT', command=root.quit, bg='red', fg='white')
    quit.pack(fill=Tkinter.X, expand=1)

    Tkinter.mainloop()


if __name__ == '__main__':
    th()