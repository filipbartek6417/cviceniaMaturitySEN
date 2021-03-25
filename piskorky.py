import tkinter

can = tkinter.Canvas(bg="white",width=600,height=600)
can.pack()

def restart():
    global x,win,pole
    can.delete("all")
    for i in range(3):
        for j in range(3):
            can.create_rectangle(i*50,j*50,50+i*50,50+j*50)
    x = True
    win = False
    pole = [[0,1,2],[3,4,5],[6,7,8]]

def save():
    global pole
    f = open('piskorky.txt','w')
    for i in range(3):
        for j in range(3):
            f.write(str(pole[i][j]))
        f.write("\n")

def klik(event):
    global x,win
    if not win and (event.x < 150) and (event.y < 150):
        a1 = event.x//50
        a2 = event.y//50
        if x:
            can.create_line(50*a1,50*a2,50+50*a1,50+50*a2)
            can.create_line(50+50*a1,50*a2,50*a1,50+50*a2)
            x = False
            pole[a1][a2] = 'x'
        else:
            can.create_oval(50*a1,50*a2,50+50*a1,50+50*a2)
            x = True
            pole[a1][a2] = 'o'
        if pole[a1][0] == pole[a1][1] == pole[a1][2] or pole[0][a2] == pole[1][a2] == pole[2][a2]:
            win = True
        if (a1 == a2 or abs(a1-a2) == 2):
            if pole[0][0] == pole[1][1] == pole[2][2] or pole[0][2] == pole[1][1] == pole[2][0]:
                win = True

restart()


can.bind("<Button-1>",klik)
tkinter.Button(text='Restart', command=restart).pack()
tkinter.Button(text='Save', command=save).pack() 


