def func(arr:list,target:int):
    res=0
    arr2=list(set(arr))
    if target==0:
        for i in arr2:
            if arr.count(i)>=2:
                res+=1
        return res
    else:
        for i in range(len(arr2)):
            for j in range(i,len(arr2)):
                if abs(arr2[i]-arr2[j])==abs(target):
                    res+=1
        return res
tests = int(input())  # 找规律
lists = []
target=[]
for i in range(tests):
    a = input()
    lists.append(list(map(int, input().split(' '))))
    target.append(int(input()))
for i in range(tests):
    print(func(lists[i],target[i]))