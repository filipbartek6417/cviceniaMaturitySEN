from re import split

f = list(map(int, split('/', input("Zadajte zlomok v tvare x/y: "))))
for i in reversed([j for j in range(1, int(max(f)))]):
    if f[0] % i == 0 and f[1] % i == 0:
        f[0] /= i
        f[1] /= i

print("{0}/{1}".format(str(int(f[0])), str(int(f[1]))))
