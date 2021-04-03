from tkinter import Canvas, Tk

main = Tk()

c = Canvas(width=1000, height=300, bg='black')
c.pack()

with open('zastavky.txt') as f:
    zastavky = [line.rstrip() for line in f]
count = 0
dlzka = len(zastavky)


def show(event):
    global c, count
    if count < dlzka:
        c.delete('all')
        c.create_text(500, 150, text=zastavky[count], font=('Arial', 100), fill='red')
        count += 1


c.bind('<Button-1>', show)
main.mainloop()
