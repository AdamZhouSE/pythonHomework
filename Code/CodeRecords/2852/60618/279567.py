n=int(input())
a=[int(k) for k in input().split()]
num=0
for i in range(0,n):
    for j in range(i,n):
        re=1
        
        if a[j]!=a[i] and (j+j-i-1)<=n-1:
            for k in range(j,j+j-i):
                if a[k]!=a[j]:
                    re=0
            if re==1:
                if num<j-i:
                    num=j-i
            re=1
    print(num)
               