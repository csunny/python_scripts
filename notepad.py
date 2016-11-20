#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@ author: magic
"""
from Tkinter import *
from tkMessageBox import *
from tkFileDialog import *
import os

filename = ''

def author():
	showinfo('作者信息', '本软件由magic开发完成')

def about():
	showinfo('版权信息.Copyright', '版权归magic所有')

def open_file():
	global filename
	filename = askopenfilename(defaultextension='.txt')
	if  not filename:
		filename = None
	else:
		root.title('Filename:' + os.path.basename(filename))
	textpad.delete(1.0, END)
	f = open(filename, 'r')
	textpad.insert(1.0, f.read())
	f.close()

def new():
	global filename
	root.title('未命名文件')
	filename = None
	textpad.delete(1.0, END)

def save():
	global filename
	try:
		f = open(filename, 'w')
		msg = textpad.get(1.0, END)
		f.write(msg)
		f.close()
	except IOError:
		saveas()

def saveas():
	f = asksaveasfile(initialfile='未命名.txt', defaultextension='.txt')
	global filename
	filename = f
	fh = open(f, 'w')
	msg = textpad.get(1.0, END)
	fh.write(msg)
	fh.close()
	root.title('Filename:' + os.path.basename(f))

def cut():
	textpad.event_generate("<< Cut >>")

def copy():
	textpad.event_generate("<< COPY >>")

def paste():
	textpad.event_generate("<< PASTE >>")

def undo():
	textpad.event_generate("<< UNDO >>")

def redo():
	textpad.event_generate("<< REDO >>")

def select_all():
	textpad.tag_add('sel', '1.0', END)

def search():
	topsearch = Toplevel(root)
	topsearch.geometry("300x200+200+250")
	label1 = Label(topsearch, text="find")
	label1.grid(row=0, column=0, padx=5)
	entry1 = Entry(topsearch, width=20)
	entry1.grid(row=0, column=1, padx=5)
	button1 = Button(topsearch, text="查找")
	button1.grid(row=0, column=2)


root = Tk()
root.title('magic node')
root.geometry("700x400+100+100")

menubar = Menu(root)
root.config(menu=menubar)

filemenu = Menu(menubar)
filemenu.add_command(label='新建', accelerator='Ctrl+N', command=new)
filemenu.add_command(label="打开", accelerator="Ctrl+O", command=open_file)
filemenu.add_command(label="保存", accelerator="Ctrl+S", command=save)
filemenu.add_command(label="另存为", accelerator="Ctrl+Shift+S", command=saveas)
menubar.add_cascade(label='文件', menu=filemenu)

editmenu = Menu(menubar)
editmenu.add_command(label="撤销", accelerator='Ctrl + z', command=undo)
editmenu.add_command(label="重做", accelerator="Ctrl + y", command=redo)
editmenu.add_separator()
editmenu.add_command(label="剪贴", accelerator="Ctrl + X", command=cut)
editmenu.add_command(label="复制", accelerator="Ctrl + C", command=copy)
editmenu.add_command(label="粘贴", accelerator="Ctrl + V", command=paste)
editmenu.add_separator()
editmenu.add_command(label="查找", accelerator="Ctrl + F", command=search)
editmenu.add_command(label="全选", accelerator="Ctrl + A", command=select_all)
menubar.add_cascade(label="编辑", menu=editmenu)

aboutmenu = Menu(menubar)
aboutmenu.add_command(label="作者", command=author)
aboutmenu.add_command(label="版权", command=about)
menubar.add_cascade(label="关于", menu=aboutmenu)

toolbar = Frame(root, height=25, bg="#FFFFFF")
shortButton = Button(toolbar, text="打开", command=open_file)
shortButton.pack(side=LEFT, padx=5, pady=5)

shortButton = Button(toolbar, text="保存", command=save)
shortButton.pack(side=LEFT)
toolbar.pack(fill=X)

status = Label(root, text='Ln20', bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

lnlabel = Label(root, width=2, bg='#CCCCCC')
lnlabel.pack(side=LEFT, fill=Y)

textpad = Text(root, undo=True)
textpad.pack(expand=YES, fill=BOTH)

scroll = Scrollbar(textpad)
textpad.config(yscrollcommand=scroll.set)
scroll.config(command=textpad.yview)
scroll.pack(side=RIGHT, fill=Y)
root.mainloop()
