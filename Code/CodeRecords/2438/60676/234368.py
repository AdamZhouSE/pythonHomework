rawList = input()
myList = []
for i in range(len(rawList)):
    if rawList[i].isnumeric():
        myList.append(int(rawList[i]))
myList.sort()
print(myList)