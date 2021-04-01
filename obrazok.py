from re import split

with open('obrazok.txt', 'r') as f:
    begin = True
    end = False
    count = 0
    toDel = []
    maybeToDel = []
    lst = [line.rstrip() for line in f]
    lst[0] = list(map(int, split(" ", lst[0])))
    for i in range(1, len(lst)):
        if lst[i] == '1' * lst[0][1]:
            count += 1
            if begin:
                toDel.append(i)
            else:
                end = True
                maybeToDel.append(i)
        elif begin:
            begin = False
        else:
            end = False
            maybeToDel = []
    toDel += maybeToDel
    for i in reversed(toDel):
        del(lst[i])
    print('White lines:', count)
    print('End result:')
    for i in lst[1:]:
        print(i)