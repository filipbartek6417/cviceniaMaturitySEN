from tkinter import Canvas, Tk
from re import split

bgColor = 'white'
main = Tk()
c = Canvas(width=1000, height=200, bg=bgColor)
c.pack()

linka = 'linka3.txt'
with open(linka, 'r') as f:
    color = split('\n', f.readline())[0]
    x = 10
    for line in f:
        line = split('\n', line)[0]
        if x == 10:
            c.create_rectangle(x, 170, x + 10, 180, fill=color)
        elif line[0] != '*':
            c.create_oval(x, 170, x + 10, 180, fill=color)
        else:
            c.create_oval(x, 170, x + 10, 180, outline=color)
        c.create_line(x + 10, 175, x + 20, 175, fill=color)
        c.create_text(x + 10, 170, angle=45, anchor='sw', text=line, font=('Arial',8))
        x += 20
    c.create_rectangle(x - 20, 170, x - 10, 180, fill=color)
    c.create_line(x - 10, 175, x, 175, fill=bgColor)

main.mainloop()
