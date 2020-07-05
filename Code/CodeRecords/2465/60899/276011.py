list0 = list(map(int, input().split(",")))
listOfh = []
for h in range(1,len(list0)+1):
    count = 0
    for i in range(0,len(list0)):
        if list0[i]>=h:
            count+=1
    if count>=h:
        listOfh.append(h)
max = -1
for h in listOfh:
    if max<h:
        max = h
print(max)