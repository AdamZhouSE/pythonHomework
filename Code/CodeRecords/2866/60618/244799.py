n=int(input())
a=[int(n) for n in input().split()]
count1=0
for i in range(0,n):
    if a[i]==1:
        count1+=1
re=count1**(n-count1)
print(re)