def func(list0:list,target:int):
    for i in range(len(list0)):
        for j in range(len(list0)):
            if j>i:
                if list0[i]+list0[j]==target:
                    return "Yes"
    return "No"
tests=int(input())
res=[]
for i in range(tests):
    target=list(map(int,input().split(" ")))[1]#所要求的和
    list0=list(map(int,input().split(" ")))
    res.append(func(list0,target))
for i in res:
    print(i)