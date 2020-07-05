def isTri(a,b,c):
    if((a+b>c)and(a+c>b)and(b+c>a)):
        return True
    return False

testNum=int(input())
for i in range(testNum):
    edgeNum=int(input())
    edges=[]
    strEdges=input().split(' ')
    for strEdge in strEdges:
        edges.append(int(strEdge))
    count=0
    if(edgeNum<3):
        print ('0')
    else:
        for i in range(edgeNum):
            for j in range(i+1,edgeNum):
                for n in range(j+1,edgeNum):
                    if(isTri(edges[i],edges[j],edges[n])):
                        count=count+1
        print(count)