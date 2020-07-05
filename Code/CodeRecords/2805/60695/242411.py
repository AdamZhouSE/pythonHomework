n = int(input())
a = input().split(" ")
count = 1
clist = []
for i in range(0, n-1):
    if int(a[i+1]) > int(a[i]):
        count += 1
    else:
        clist.append(count)
        count = 1
clist.append(count)
clist = sorted(clist)
clist.reverse()
print(clist[0])