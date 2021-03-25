from tkinter import Canvas, Tk
from random import choice

delenec, delitel = int(input('Delenec: ')), int(input('Delitel: '))
text = str(delenec) + ' : ' + str(delitel) + ' = ' + str(delenec // delitel) + '  zvysok ' + str(delenec % delitel)

main = Tk()
can = Canvas(width=500, height=500, bg='white')
can.pack()
can.create_text(250, 40, text=text, font=('Arial', 30), fill='green')
bezzvysok = delenec - delenec % delitel
for i in range(delenec):
    if i % delitel == 0:
        randomColor = '#'+''.join([choice('1234567890ABCDEF') for j in range(6)])
    if i < bezzvysok:
        can.create_oval(250 + i * 10, 70, 260 + i * 10, 80, fill=randomColor)
    else:
        can.create_oval(250 + i * 10, 70, 260 + i * 10, 80, outline=randomColor)

main.mainloop()
