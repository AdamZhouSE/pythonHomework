def find(nums,a,s):
    su=0
    ans=[]
    for m in range(s - 1):
        su= items[m]
        for n in range(m + 1, s):
            su = su + items[n]
            if (su == a):
                ans.append(m + 1)
                ans.append(n + 1)
                return ans
    return []

testNum=int(input())
for i in range (testNum):
    srcs=input().split()
    size=int(srcs[0])
    num=int(srcs[1])
    rawInputs=input().split(' ')
    items=[]
    for rawInput in rawInputs:items.append(int(rawInput))
    sum=0
    ans=find(items,num,size)
    if(len(ans)==0):print('-1')
    else:print(' '.join(str(x)for x in ans))