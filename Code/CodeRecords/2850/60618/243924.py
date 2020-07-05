n = int(input())
a=[int(n) for n in input().split()]
count0=0
count1=0
for i in range(0,n):
    if a[i]==0:
        count0+=1
    else:
        count1+=1
count02=count0
count12=count1
for i in range(0,n):
    for j in range(i,n):
        if a[j]==0:
            count12+=1
        else:
            count12-=1
        if count12>count1:
            count1=count12
print(count12)
            