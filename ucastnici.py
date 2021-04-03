from re import split

with open('ucastniciMena.txt', 'r') as mena, open('ucastniciPoradie.txt') as poradie:
    m = [line.rstrip() for line in mena]
    p = [int(line.rstrip()) for line in poradie]
    dlzka = len(m)
    print('Pocet ucastnikov:',dlzka)
    a = input('Zadajte meno účastníka ')
    najh = ''
    print('\nNajhorsi ucastnici:')
    for i in range(dlzka):
        if m[i] == a:
            najh = p[i]
        if p[i] > (dlzka-4):
            print(m[i])
    print()
    if najh != '':
        print(a+" skoncil na "+str(najh)+". mieste")
    else:
        print("Taky ucastnik nie je!")