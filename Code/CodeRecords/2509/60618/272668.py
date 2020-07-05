n=int(input())
li=[int(k) for k in input().split()]
m=int(input())
construction=[['']]*m
for i in range(0,m):
    construction[i]=input().split()
    if construction[i][0]=='add':
        li.append(int(construction[i][1]))
    else:
        for j in range(1,len(li)):
            for k in range(0,len(li)-j):
                if li[k]>li[k+1]:
                    li[k],li[k+1]=li[k+1],li[k]
        if len(li)%2==0:
            print(li[len(li)//2-1])
        else:
            print(li[len(li)//2])
            