lists = list(eval(input()))
k = int(input())
alist = list(set(lists))
alist.sort()
distance = set()
if len(distance)>len(alist):
    distance.add(0)
for i in range(len(alist)):
    for j in range(i+1,len(alist)):
        distance.add(alist[j]-alist[i])
dis = list(distance)
print(dis[k-1])