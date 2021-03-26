line = ''
count = 0
linecount = ''
passs = False
with open('hlavo.txt', 'r') as f:
    linka = f.readline()[:-1]
    while linka != '':
        for i in linka:
            if i == '0':
                line += '_'
                if passs:
                    linecount = linecount+str(count)+' '
                    count = 0
                    passs = False
            else:
                line += 'X'
                count += 1
                passs = True
        if line[-1] == 'X':
            linecount = linecount + str(count) + ' '
        line += '\n'
        linecount += '\n'
        count = 0
        passs = False
        linka = f.readline()[:-1]
    print(line)
    print(linecount)