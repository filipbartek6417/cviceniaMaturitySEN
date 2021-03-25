#!/usr/bin/python3

from re import split
from tkinter import Canvas, Button, Listbox, Menu, Entry, Tk, simpledialog, Toplevel, Text
from korytnackaObject import Kora
from stack import Stack
from prikaz import Prikaz


def saveCmd(name):
    global cmds, cmdWindow, cmdText
    if name not in cmds.keys():
        lst.insert(0, name)
    cmds[name] = cmdText.get('1.0', 'end-1c')
    cmdWindow.destroy()


def saveToFile(f=open('pokus.txt', 'w')): # works Okay
    for key in cmds.keys():
        f.write(key + ":" + cmds[key])
    f.close()


def loadFromFile(f=open('pokus.txt', 'r')): # startup clears the file, dunno why
    global cmds
    cmds = {}
    l = f.readline()
    print(l)
    while l != "":
        cmds[split(l, "[:")[0]] = split(l, "[:")[1]
        l = f.readline()
    print(cmds)


def newCmd():
    newName = simpledialog.askstring('New Command', 'Enter new command name')
    if newName is None or newName == '':
        return
    editCmd(newName)


def editCmd(name):
    global cmds, cmdWindow, cmdText
    cmdWindow = Toplevel()
    cmdWindow.title('Command ' + name)
    cmdText = Text(cmdWindow)
    if name in cmds.keys():
        cmdText.insert('end', cmds[name])
    cmdText.pack()
    Button(cmdWindow, text='Save command', command=lambda: saveCmd(name)).pack()


def doubleClick(event):
    cur = lst.curselection()
    cmd = lst.get(cur)
    editCmd(cmd)


def interpret():
    pass


def cliKey(event):
    if event.keysym == 'Return':
        s.push(Prikaz(typ='n', text=cli.get()))  # s.push()
        print(s)


main = Tk()
c = Canvas(main, height=400, width=400)
c.grid(column=0, row=0)

cli = Entry(main, font='Arial 15')
cli.grid(column=0, row=1, sticky='nwes')
cli.bind("<Key>", cliKey)

lst = Listbox(main)
lst.grid(column=1, row=0, columnspan=2, sticky='nwes')
lst.bind('<Double-Button-1>', doubleClick)

add = Button(main, text='New', command=newCmd)
add.grid(column=1, row=1)

rm = Button(main, text='Delete')
rm.grid(column=2, row=1)

save = Button(main, text='Save', command=saveToFile)
save.grid(column=3, row=1)

load = Button(main, text='Load', command=loadFromFile)
load.grid(column=4, row=1)

m = Menu(main)
main.config(menu=m)

file = Menu(m)
file.add_command(label='Save')
file.add_command(label='Load')
m.add_cascade(label='File', menu=file)

k = Kora(c)
s = Stack()

cmds = {}

k.fwd(100)
k.left(30)
k.fwd(20)
k.right(60)
k.fwd(10)
k.right(320)
k.fwd(10)
k.changePC("green")
k.fwd(10)
k.changeHP(3)
k.fwd(10)
# k.erase()
# k.home(c) #tu treba vybrat zatial canvas, casom sa to da opravit ak bude treba
# k.fwd(50)

main.mainloop()
