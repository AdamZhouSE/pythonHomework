lists = list(eval(input()))
k = int(input())
aset = set(lists)
distance = set()
if len(lists)>len(aset):
    distance.add(0)
alist = list(aset)
for i in range(len(alist)):
    for j in range(i+1,len(alist)):
        distance.add(alist[j]-alist[i])
dis = list(distance)
print(dis[k-1])