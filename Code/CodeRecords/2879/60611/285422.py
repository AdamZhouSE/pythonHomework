number=int(input())
l=[]
for i in range(pow(number,2)):
    l.append(list(map(int,input().split(" "))))
tag1=[0 for i in range(number)]
tag2=[0 for i in range(number)]
result=[]
for i in range(pow(number,2)):
    if tag1[l[i][0]-1]==0 and tag2[l[i][1]-1]==0:
        result.append(i+1)
        tag1[l[i][0]-1]=1
        tag2[l[i][1]-1]=1
for i in range(len(result)-1):
    print(result[i],end=" ")
print(result[-1])