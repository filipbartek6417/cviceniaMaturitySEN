from re import split

with open('reklama.txt', 'r') as f:
    line = f.readline()
    while line != '':
        x = split('@', line)
        print(x)
        if len(x) > 2 or '.' not in x[1] or x[0] == '':
            pass
        else:
            print(line)
        line = f.readline()