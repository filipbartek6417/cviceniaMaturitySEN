from re import split

f = open('prehadzovanie.txt', 'r')
l = f.readline()

while l != '':
    maxLength = 0
    lengths = []
    x = split(" |\n", l)
    del(x[-1])
    for i in x:
        lenHere = len(i)
        lengths.append(lenHere)
        if lenHere > maxLength:
            maxLength = lenHere
    cipher = [''] * maxLength
    for i in x:
        for j in range(len(i)):
            cipher[j] += i[j]
    print(cipher)
    print(lengths)
    l = f.readline()
