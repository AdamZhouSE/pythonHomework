t=int(input())
for i in range(t):
    nx=input()
    nums=input().split(' ')
    nums = [int(x) for x in nums]
    n=int(nx.split(' ')[0])
    x=int(nx.split(' ')[1])
    store=[];
    for i in range(n):
        if nums[i]%x==0:
            store.append(nums[i])
    if len(store)==0:
        print(0)
    elif len(store)==1:
        print(store[0])
    else:
        for i in range(len(store)):
            store[0]=store[0]|store[i]
        print(store[0])