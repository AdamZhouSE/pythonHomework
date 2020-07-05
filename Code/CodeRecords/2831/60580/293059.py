num = int(input())
tempList = input().split()
busList = []
all = 0
for var in tempList:
    all += int(var)
    busList.append(int(var))
to = input().split()
i = 1
l = []
l.append(0)
temp = 0
while i < num:
    temp = temp + busList[i - 1]
    l.append(temp)
    i += 1
start = int(to[0]) - 1
end = int(to[1]) - 1
if start >= end:
    start, end = end, start
path = l[end] - l[start]
if all - path >= path:
    print(path)
else:
    print(all - path)