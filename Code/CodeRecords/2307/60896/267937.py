a=eval(input())
for t in range(0,a):
    e=False
    b=input()
    c=input()
    nums=[]
    c=c.split(' ')
    for i in c:
        nums.append(int(i))
    if len(nums)==1:
        print(nums[0])
        break
    numDic = {}
    for i in nums:
        if i in numDic:
            numDic[i] += 1
            if numDic.get(i)>=(len(nums)+1)/2:
                print(i)
                e=True
        else:
            numDic[i] = 1
    if(not e):print(-1)
