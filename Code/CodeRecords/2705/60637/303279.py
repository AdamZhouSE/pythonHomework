edges=eval(input())
degrees=[0]*len(edges)
for i in edges:
    degrees[i[1]-1]+=1
target=1
if(degrees[0]!=1):
    target=degrees.index(2)+1
for i in range(len(edges)-1,-1,-1):
    if(edges[i][1]==target):
        print(edges[i])
        break