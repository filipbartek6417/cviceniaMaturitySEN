from tkinter import Canvas, Tk
from re import split

main = Tk()
can = Canvas(height=400, width=400, bg='white')
can.pack()

f = open('spoplatnenie.txt', 'r')
can.create_text(200,50,text=f.readline(),anchor='n')
x = list(map(int, split(' |\n', f.readline())))
y = ['Ano', 'Nie', 'Neviem']
longest = x.index(max(x))
for i in range(len(x)):
    if i == longest:
        color = 'red'
    else:
        color = 'blue'
    string = str(i+1)+') '+y[i]+' - '+str(x[i])
    can.create_text(200,75+i*25,text=string)
    can.create_rectangle(250,60+i*25,250+x[i],90+i*25,fill=color)

main.mainloop()