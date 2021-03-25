import re

f = open('mena.txt')

l = f.readline()
count = 0
multi = 0
names = []
lenPriezvisko = ''
lenMeno = ''
cor = ''
prz = ''
complete = []
while l != '':
    s = re.split(" |\n", l)
    del(s[-1])
    names.append(s)
    count += 1
    l = f.readline()
f.close()
print(int(count/2))
for i in range(int(count/2)):
    if len(names[i]) > 1:
        multi += 1
    cor = " ".join(names[i])
    prz = " ".join(names[i+int(len(names)/2)])
    if len(cor) > len(lenMeno):
        lenMeno = cor
    if len(prz) > len(lenPriezvisko):
        lenPriezvisko = prz
    complete.append(cor+' '+prz)

print(multi)
print(lenMeno)
print(lenPriezvisko)
print(complete)

f2 = open('menaEnd.txt','w')
for i in complete:
    f2.write(i+'\n')
f2.close()
