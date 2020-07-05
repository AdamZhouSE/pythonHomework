def func(arr:list,ope:list,target:int):
    length=len(arr)
    ll=len(ope)
    for i in ope:
        if i[0]==0:
            begin=i[1]-1
            end=i[2]
            temp=arr[begin:end]
            temp.sort()
            arr=arr[0:begin]+temp+arr[end:]
        if i[0]==1:
            begin = i[1] - 1
            end = i[2]
            temp = arr[begin:end]
            temp.sort()
            arr = arr[0:begin] + temp[::-1] + arr[end:]
    return arr[target-1]
first=input()
tests=int(first.split(' ')[1])
lists=list(map(int,input().split(' ')))
operation=[]
for i in range(tests):
    operation.append(list(map(int,input().split(' '))))
target=int(input())
print(func(lists,operation,target))