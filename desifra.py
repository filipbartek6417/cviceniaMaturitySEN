a = 'KRRSeQbjtKzZoiFF0shWV5TTnk3kiflf3XtMPfu9'

listOfChars = {}
length = 0

for i in a:
    x = ord(i)
    if 65 <= x <= 90 or 97 <= x <= 122:
        if i not in listOfChars:
            listOfChars[i] = 1
        else:
            listOfChars[i] += 1
        length += 1
print(listOfChars)
print(max(listOfChars.values()))
