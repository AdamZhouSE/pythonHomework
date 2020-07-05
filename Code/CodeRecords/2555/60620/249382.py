n=int(input())
a=list(map(int,input().split()))
num=0
for i in range(n):
    for j in range(i,n):
        for k in range(j,n):
            if(a[i]<a[j] and a[j]<a[k]):
                num+=1
print(num,end="")