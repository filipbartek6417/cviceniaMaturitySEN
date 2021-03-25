from tkinter import Canvas, Tk
from re import split

main = Tk()
c = Canvas(height=500, width=500, bg='white')
c.pack()
with open('obrklop.txt', 'r') as f:
    properties = list(map(int, split(" |\n", f.readline())[0:2]))
    for j in range(properties[0]):
        line = split("\n", f.readline())[0]
        for i in range(len(line) - 1, 0, -1):
            if line[i] == '0':
                c.create_rectangle(20 + i * 20, 20 + j * 20, 40 + i * 20, 40 + j * 20, fill='black')
            else:
                c.create_rectangle(20 + i * 20, 20 + j * 20, 40 + i * 20, 40 + j * 20, fill='white')

main.mainloop()
