a = input("Input: ")
colors = ['red','orange','yellow','green','blue','violet','brown']


parents = 0
for i in a:
    if i == '(':
        parents += 1
    elif i == ')':
        parents -= 1
    if parents < 0:
        break
if parents == 0:
    print('good')
else:
    print('bad')