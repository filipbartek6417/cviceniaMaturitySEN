slova = ['maringotka', 'kaufland']

for slovo in slova:
    cur = ['*'] * len(slovo)
    count = 0
    while '*' in cur:
        mistake = True
        print("".join(cur))
        guess = input("Zadaj pismeno: ")
        for i in range(len(slovo)):
            if guess == slovo[i]:
                cur[i] = guess
                mistake = False
        if mistake:
            print("Toto pismeno tam nie je")
            count += 1
    print("Gratulujeme, hladane slovo je " + slovo)
    print("Pocet chyb: " + str(count))
    print(input("Stlac enter pre pokracovanie: "))

print("Koniec hry")