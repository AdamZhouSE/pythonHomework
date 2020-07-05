s=input().split(' ')
n=int(s[0])
m=int(s[1])
li1=[]
li2=[]
sum1=0
sum2=0
for i in range(n):
    j=input().split(' ')
    li1.append(int(j[0]))
    li2.append(int(j[1]))
    sum1=sum1+li1[i]
    sum2=sum2+li2[i]
index=0
if(sum2>m):
    print(-1)
    exit()
if(sum1<=m):
    print(0)
else:
    for k in range(n):
        for j in range(k+1,n):
            if(li2[k]<li2[j]):
                a=li2[k]
                b=li1[k]
                li1[k]=li1[j]
                li2[k]=li2[j]
                li1[j]=b
                li2[j]=a
    for i in range(0,n):
        sum1=sum1-(li1[i]-li2[i])
        index+=1
        if(sum1<=m):
            print(index)
            exit()