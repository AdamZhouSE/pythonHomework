k,m=map(int,input().split())
set=[1]
i=0
while i<k:
    set.append(2*set[i]+1)
    set.append(4*set[i]+5)
    set=sorted(set)
    i+=1
set=set[:k]
num="".join(str(i) for i in set)
print(num)
num=list(num)
n=len(num)-m
maxNum=-1
re=[]
while n>0:
    i=maxNum+1
    max=num[i]
    for x in range(i,len(num)-n+1):
        if num[x]>max:
            max=num[x]
            maxNum=x
    re.append(max)
    n=n-1
print("".join(re))