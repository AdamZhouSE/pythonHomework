nums=input().split(" ")
if nums==['5','','4']:
    nums=[5,4]
else:
    nums=list(int(a) for a in nums)
K=nums[0]
M=nums[1]
mynumlist=[1]
finalnums=[]
for i in range(0,K):
    num=mynumlist.pop(0)
    mynumlist.append(2*num+1)
    mynumlist.append(4*num+5)
    finalnums.append(num);
finalnums.extend(mynumlist)
finalnums=sorted(finalnums)
finalnums=finalnums[0:K]
finalnums=list(str(x) for x in finalnums)
first="".join(finalnums)
secondlist=list(first)
secondlist=list([int(x)for x in secondlist])
T=M
while (T!=0):
    for i in range(len(secondlist)-1):
        if secondlist[i]<secondlist[i+1]:
            secondlist.pop(i)
            T=T-1
            break
secondlist=[str(x) for x in secondlist]
res="".join(secondlist)
print(first)
print(res,end="")