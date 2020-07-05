x = input()
xlist = x.split(" ")
n = int(xlist[0])
m = int(xlist[1])

x = input()
xlist = x.split(" ")
sweets = [int(xlist[i]) for i in range(len(xlist))]

temp = sweets
while max(temp) > 0:
    for i in range(n):
        temp[i] -= m
        if temp[i] <= 0:
            temp[i] = 0
        if temp.count(0) == n - 1:
            print(temp.index(max(temp)) + 1)
            break
    else:
        continue
    break
