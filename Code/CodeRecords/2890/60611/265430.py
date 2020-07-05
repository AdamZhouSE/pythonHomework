num=list(map(int,input().split()))
x,y=num[1],num[2]
l=[]
for i in range(num[0]):
    l.append(list(map(int,input().split())))
    l[i][0]=l[i][0]-x
    l[i][1]=l[i][1]-y
tag=[0 for i in range(num[0])]
for i in range(num[0]):
    for j in range(i+1,num[0]):
        if l[i][0]*l[j][1]==l[i][1]*l[j][0]:
            tag[j]=1
print(tag.count(0))