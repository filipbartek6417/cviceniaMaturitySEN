a = input()
out = ''
com = [0,0,0,0,0,0,0,0,0,0]
for i in a:
    x = ord(i)
    if 65 <= x <= 90:
        x -= 65
        out += str(x//3+1)*(x%3+1)+' '
        com[x//3+1] += (x%3+1)
    elif x == 32:
        out += '0 '
        com[0] += 1
    else:
        out = 'Invalid'
        break
    
print(out)
m = max(com)
print('Najcastejsie tlacidlo:',[i for i, j in enumerate(com) if j == m])
