import re

f = open('bezanie.txt')
d = []
l = f.readline()
while l != '':
    s = re.split(" |\n",l)
    d.append([s[0],int(s[1]),int(s[1])//60])
    l = f.readline()   
d.sort(key=lambda x: x[1])
print("Najrychlejsi:",d[0][0],"\nNajpomalsi:",d[-1][0])
a = int(input("pocet ludi:"))
for i in range(a):
    print(d[i][0])
mnt = 0
for i in range(len(d)):
    if d[i][2] != mnt:
        mnt = d[i][2]
        print("V "+str(mnt)+". minute dobehli:")
    print("-   ",d[i][0])
