alist = input().split(",")
for i in range(len(alist)):
    alist[i] = int(alist[i])
alist.sort()
print(alist[0])