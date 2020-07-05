n=int(input())
list1=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
res=0
for i in list1:
    if i > n:
        break
    res+=1
mod=1000000007
ans=1
for i in range(1,res+1):
    ans*=i
    ans%=mod
for i in range(1,n-res+1):
    ans*=i
    ans%=mod
print(ans)