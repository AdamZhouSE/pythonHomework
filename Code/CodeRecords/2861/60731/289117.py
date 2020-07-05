n=int(input())
a=list(map(int,input().split()))
a.sort()
num=0
for i in range(0,n,2):
    num+=(a[i+1]-a[i])
print(num)