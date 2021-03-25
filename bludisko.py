from tkinter import Canvas, Button

c = Canvas(bg='white',height=400,width=400)
c.pack()
first = True
x1,y1 = 0,0

for i in range(10):
    for j in range(10):
        c.create_rectangle(i*20,j*20,(i+1)*20,(j+1)*20)

def click(event):
    global first,x1,y1
    if first:
        x1,y1 = event.x//20,event.y//20
        first = False
    else:
        first = True
        if x1 == event.x//20:
            for i in range(y1,event.y//20+1):
                c.create_rectangle(x1*20,i*20,(x1+1)*20,(i+1)*20,fill='blue')    
        elif y1 == event.y//20:
            for i in range(x1,event.x//20+1):
                c.create_rectangle(i*20,y1*20,(i+1)*20,(y1+1)*20,fill='blue')

def init():
    c.delete('all')
    first = True
    x1,y1 = 0,0
    for i in range(10):
        for j in range(10):
            c.create_rectangle(i*20,j*20,(i+1)*20,(j+1)*20)



c.bind('<Button-1>',click)
Button(text='Clear',command=init).pack()
