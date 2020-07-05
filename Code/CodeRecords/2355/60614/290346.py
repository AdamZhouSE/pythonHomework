length=int(input().split()[0])
nodes=[int(x) for x in input().split()]
edges=[]
for i in range(length-1):
    edges.append([int(x) for x in input().split()])
minimum=66
for i in range(length-1):
    set1=[edges[i][0]]
    set2=[edges[i][1]]
    for j in range(length-1):
        if j!=i:
            if edges[j][0] in set1:
                set1.append(edges[j][1])
            elif edges[j][0] in set2:
                set1.append(edges[j][1])
            elif edges[j][1] in set1:
                set1.append(edges[j][0])
            elif edges[j][1] in set2:
                set1.append(edges[j][0])
    sum1=0
    sum2=0
    for j in set1:
        sum1+=nodes[j-1]
    for j in set2:
        sum2+=nodes[j-1]
    minimum=min(minimum,abs(sum2-sum1))
print("Case 1: "+str(minimum))