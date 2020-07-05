n=int(input())
a=list(map(int,input().split()))
a.sort()
sum=0
for i in range(n//2):
    tmp=a[i]+a[n-i-1]
    sum+=tmp*tmp
print(sum)