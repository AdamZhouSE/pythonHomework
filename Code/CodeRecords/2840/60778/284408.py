k=list(map(int,input().split()))[1]
nums=input().split()
res=0
for i in nums:
    if(i.count('4')+i.count('7')<=k):
        res+=1
print(res)