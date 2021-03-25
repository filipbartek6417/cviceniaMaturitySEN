conv = ''
up = True
words = 1
for i in input():
    if ord(i) == 32:
        up = not up
        words += 1
    elif up:
        conv += i.upper()
    else:
        conv += i.lower()
print(words)
print(conv)
up = True
orig = ''
for i in conv:
    if up != i.isupper():
        up = not up
        orig += ' '
    orig += i.upper()
print(orig)
