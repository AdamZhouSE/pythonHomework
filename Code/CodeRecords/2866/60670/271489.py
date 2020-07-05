n=int(input())
nuts=list(map(int,input().split()))
last=nuts.index(1)
nums=1
for i in range(last+1,n):
    if nuts[i]==1:
        nums=nums*(i-last)
        last=i
print(nums)