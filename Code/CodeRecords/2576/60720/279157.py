list0=input().split(',')
target=int(input())
l=len(list0)
list0=[int(list0[i]) for i in range(len(list0))]
list0.sort()
base=0
no=0
isF=False
def su(base):
    index = 0
    sum=0
    for i in range(l):
        if base <= list0[i]:
            index = i
            break
    for i in range(0,index):
        sum+=base-list0[i]
    return base*l-sum
for i in range(l):
    sum=0
    if list0[i]*l>target:
        for j in range(0,i):
            sum+=list0[i]-list0[j]
        if list0[i]*l<target+sum:
            base=list0[i]+1
            break
        if list0[i]*l==target+sum:
            print(list0[i])
            isF=True
            break
if not isF:
    result=0
    while(su(base)<target):
        result=su(base)
        base+=1
    if result-target<target-su(base-1):
        print(base-1)
    else:
        print(base)