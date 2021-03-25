import re,tkinter

f = open('bus_vizualizacia.txt')
kap = int(f.readline())
zas = []
line = f.readline()
while line != '':
    s = re.split(' |\n',line)
    del(s[-1])
    s[2] = " ".join(s[2:])
    del(s[3:])
    zas.append(s)
    line = f.readline()

c = tkinter.Canvas()
c.pack()

for i in range(len(zas)):
    c.create_text(10,20+i*20,text=zas[i][2],anchor="nw")

num = 0
trav = 0

def show(event):
    global num,kap,trav,zas
    col = 'green'
    trav += int(zas[num][0])
    trav -= int(zas[num][1])
    if trav > kap:
        col = 'red'
    c.create_rectangle(100,20+num*20,100+kap,40+num*20,outline='black',width=2)
    c.create_rectangle(100,20+num*20,100+trav,40+num*20,fill=col)
    num += 1



c.bind('<Button-1>',show)
