def func(arr:list,target:int):
    res = ''
    l=0
    s=''.join(arr)
    length=len(arr)
    for i in range(1,length+1):
        for j in range(length+1-i):
            temp=s[j:j+i]
            temp2=''+temp
            if len(set(temp))==target and len(temp2)>l:
                res=temp2
                l=len(res)
    return l


tests = int(input())  # 找规律
lists = []
target=[]
for i in range(tests):
    lists.append(list(input()))
    target.append(int(input()))
for i in range(tests):
    print(func(lists[i],target[i]))