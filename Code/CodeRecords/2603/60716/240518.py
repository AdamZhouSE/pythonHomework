lists = list(eval(input()))
k = int(input())
alist = list(set(lists))
alist.sort()
distance = {}
for i in range(len(alist)):
    for j in range(i+1,len(alist)):
        distance.update(alist[j]-alist[i])
dis = list(distance)
print(dis[k-1])