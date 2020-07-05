k,m=map(int,input().split())
nums=[1]
n=k
k=int(k/2)+2
i=0
while k>0:
    nums.append(nums[i]*2+1)
    nums.append(nums[i]*4+5)
    nums.sort()
    i+=1
    k-=1
l=nums[0:n]
s=''.join(str(i) for i in l)
print(s)
s=list(s)
m=len(s)-m
ind=-1
res=""
while m>0:
    tem=ind+1
    for i in range(ind+1,len(s)-m+1):
        if s[tem]<s[i]:
            tem=i
    ind=tem
    res+=str(s[ind])
    m-=1
print(res,end="")