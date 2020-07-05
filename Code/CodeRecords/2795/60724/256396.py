number=int(input())
numlist=input().split()
numlist=[int(x) for x in numlist]
numlist.sort()
num=set(numlist)
numlist=list(num)
res=-1
if len(num)==1:
    res=0
elif len(num)==2:
    res=(numlist[1]-numlist[0])
    if res%2==0:
        res=(numlist[1]-numlist[0])/2
elif len(num)==3:
    if numlist[2]+numlist[0]==2*numlist[1]:
        res=numlist[1]-numlist[0]
else:
    res=-1
print(res)