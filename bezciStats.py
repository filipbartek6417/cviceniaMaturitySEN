from re import split

with open('bezciStats.txt', 'r') as f:
    count = 0
    maxDistance = -1
    maxJumper = ''
    line = f.readline()
    countries = {}
    while line != '':
        x = split(" |\n", line)
        print(x)
        del(x[-1])
        for i in x[2:]:
            if int(i) > maxDistance:
                maxJumper = x[0]
                maxDistance = int(i)
        if x[1] not in countries.keys():
            countries[x[1]] = [x[0]]
        else:
            countries[x[1]].append(x[0])
        count += 1
        line = f.readline()
    print(count)
    print(maxJumper, maxDistance)
    print(countries)