lists = list()
input()
temp = input()
templist = list(eval(temp[0:len(temp-1)]))
lists.append(templist)
for i in range(len(templist)-2):
    temp = input()
    templist = list(eval(temp[0:len(temp-1)]))
    lists.append(templist)
templist = list(eval(input()))
lists.append(templist)
print(lists)