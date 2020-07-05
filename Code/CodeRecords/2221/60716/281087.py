def popular(order:int):
    if not order in fans:
        fans.append(order)
        for j in lists:
            if j[0]==order:
                popular(j[1])
    else:
        return 

n,m = map(int,input().split())
lists = list()
hello = list()
for i in range(m):
    a,b = map(int,input().split())
    lists.append([b,a])
for i in range(n):
    fans = list()
    popular(i+1)
    temp = list(set(fans))
    temp.remove(i+1)
    hello.append(temp)
index = 0
for i in range(len(hello)):
    if len(hello[i])==n-1: index+=1
print(index)
