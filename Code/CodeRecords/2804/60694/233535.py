x = input()
xlist = x.split("+")
xlist = [int(xlist[i]) for i in range(len(xlist))]
xlist.sort()

n = 0
while n < len(xlist):
    print(xlist[n], end='')
    if n != len(xlist) - 1:
        print("+", end='')
    n = n + 1
print()