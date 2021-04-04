from tkinter import *

main = Tk()

c = Canvas(width=1000, height=300, bg='black')
c.pack()

with open('zastavky.txt') as f:
    zastavky = [line.rstrip() for line in f]

zastavky[-1] += '   konecna zastavka'
count = 0
dlzka = len(zastavky)
fps = 1000


def show(event):
    global c, count, text
    if count < dlzka:
        c.delete('all')
        text = c.create_text(1000, 150, text=zastavky[count], font=('Arial', 100), fill='red', anchor="w", tags="text")
        count += 1
        move()

def move():
    global fps
    x1, y1, x2, y2 = c.bbox("text")
    if x2 < 0:
        c.coords("text", 1000, 150)
    else:
        c.move("text", -2, 0)
    c.after(50, move)

c.bind('<Button-1>', show)
main.mainloop()
