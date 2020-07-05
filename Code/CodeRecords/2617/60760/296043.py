def func(strs:str,k:int):
    length=len(strs)
    res=0
    for i in range(1,length+1):
        for j in range(length-i+1):
            temp=strs[j:j+i]
            if temp.count('1')==k:
                res+=1
    return res
tests=int(input())
lists=[]
ks=[]
for i in range(tests):
    temp=input().split(' ')
    lists.append(temp[0])
    ks.append(int(temp[1]))
for i in range(tests):
    print(func(lists[i],ks[i]))