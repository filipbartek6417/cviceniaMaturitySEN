from tkinter import Canvas, Tk

main = Tk()
c = Canvas(height=500, width=600)
c.pack()
specials = ['C','+','-','=']
k = 50

def reset():
    global display, cache, operation
    display = '0'
    cache = 0
    operation = ''
reset()

mytext = c.create_text(10, 10, font=('Arial', 40), text=display, anchor='nw')
def showMytext():
    global mytext, display
    c.delete(mytext)
    mytext = c.create_text(10,10,font=('Arial', 40),text=display,anchor='nw')

def equals():
    global display, cache, operation
    if operation == '+':
        cache += int(display)
    elif operation == '-':
        cache -= int(display)
    display = str(cache)
    cache = 0

for i in range(10):
    c.create_rectangle(i*50,20+k,i*50+50,70+k)
    c.create_text(i*50+25,45+k,text=str(i))
for i in range(len(specials)):
    c.create_rectangle(i*50,70+k,i*50+50,120+k)
    c.create_text(i*50+25,95+k,text=specials[i])

def click(event):
    global display, cache, operation
    if 70 < event.y < 120 and event.x < 500:
        display += str(event.x//50)
        if len(display) > 0 and display[0] == '0':
            display = display[1:]
        showMytext()
    if 120 < event.y < 170:
        if event.x < 50:
            reset()
        elif event.x < 100:
            operation = '+'
            cache = int(display)
            display = '0'
        elif event.x < 150:
            operation = '-'
            cache = int(display)
            display = '0'
        elif event.x < 200:
            equals()
        showMytext()

c.bind('<Button-1>',click)
main.mainloop()