nums=input().split(" ")
a=int(nums[0])
b=int(nums[1])
alist=input().split(" ")
alist=list(int(x) for x in alist)
alist.sort()
blist=input().split(" ")
blist=list(int(x) for x in blist)
result=[0]*b
for i in range(b):
    for j in range(a):
        if(alist[j]<=blist[i]):
            result[i]+=1
res=""
for i in range(0,b-1):
    res=res+str(result[i])+" "
res=res+str(result[b-1])
print(res)