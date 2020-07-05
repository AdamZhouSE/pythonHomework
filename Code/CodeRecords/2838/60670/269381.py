n=int(input())
a=sorted(list(map(int,input().split())))
summ=0
for i in range(0,n//2):
    tmp=a[i]+a[n-i-1]
    summ+=tmp*tmp
print(summ)