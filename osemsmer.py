from re import split

f = open('osemsmer.txt', 'r')
g = open('osemsmerslova.txt', 'r')

o = []
line = f.readline()
while line != '':
    cur = split(' |\n', line)
    del (cur[-1])
    o.append(cur)
    line = f.readline()

line = g.readline()
while line != '':
    isIn = True
    xOffset = []
    yOffset = []
    for i in range(8):
        for j in range(8):
            if o[i][j] == line[0]:
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        if 0 < i + k < 7 and 0 < j + l < 7 and o[i + k][j + l] == line[1]:
                            xOffset.append([i, k])
                            yOffset.append([j, l])
    for x in range(len(xOffset)):
        for i in range(2, len(line)):
            x1 = xOffset[x][0] + i * xOffset[x][1]
            y1 = yOffset[x][0] + i * yOffset[x][1]
            if 0 < x1 < 7 and 0 < y1 < 7 and line[i] != o[x1][y1]:
                isIn = False
                break
        if isIn:
            break
    print(isIn)
    line = g.readline()

# options: find first letter and search the vicinity
# or: find both first and last letter -> might be faster
