M,N=map(int,input().split())
a=[0,0,0,0,0,0,0,0,0,0]
for i in range(M,N+1):
    j=i
    while j>0:
        a[j%10]+=1
        j=j//10
for i in range(len(a)-1):
    print(a[i],end=' ')
print(a[len(a)-1],end='')