length=int(input().split()[0])
nodes=[int(x) for x in input().split()]
edges=[]
for i in range(length-1):
    edges.append([int(x) for x in input().split()])
minimum=66
for i in range(length-1):
    set1=[edges[i][0]]
    set2=[edges[i][1]]
    temp=[]+edges
    del temp[i]
    j=0
    while len(temp)>0:
        if temp[j][0] in set1:
            set1.append(temp[j][1])
            del temp[j]
        elif temp[j][0] in set2:
            set2.append(temp[j][1])
            del temp[j]
        elif temp[j][1] in set1:
            set1.append(temp[j][0])
            del temp[j]
        elif temp[j][1] in set2:
            set2.append(temp[j][0])
            del temp[j]
        if len(temp)>0:
            j=(j+1)%len(temp)
    sum1=0
    sum2=0
    for j in set1:
        sum1+=nodes[j-1]
    for j in set2:
        sum2+=nodes[j-1]
    minimum=min(minimum,abs(sum2-sum1))
print("Case 1: "+str(minimum))