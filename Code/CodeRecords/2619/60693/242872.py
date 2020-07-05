cases=int(input())
for i in range(cases):
    nums=list(map(int,list(input())))
    n=len(nums)
    prods=[]
    for i in range(n):
        prods.append(nums[i])
        for j in range(i+1,n):
            prods.append(prods[-1]*nums[j])
    if len(set(prods))<len(prods):print('0')
    else:print('1')