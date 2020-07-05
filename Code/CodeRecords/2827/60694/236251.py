num = int(input())


x = input()
xlist = x.split(" ")
resList = [int(xlist[i]) for i in range(len(xlist))]

resList.sort()
for i in range(len(resList)):
    print(resList[i], end="")
    if i != len(resList) - 1:
        print(" ", end="")
print()


