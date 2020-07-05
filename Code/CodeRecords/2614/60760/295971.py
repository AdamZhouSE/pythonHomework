def func(arr:list):
    res=0
    n=len(arr[0])
    for i in range(n):

            temp=arr[1][i]+arr[2][i]
            if arr[0].count(temp)>0:
                res+=1
    return res
tests=int(input()) #找规律
arr=[]
lists=[]
sizes=[]
for i in range(tests):
    sizes.append(int(input()))
    for i in range(3):
        arr.append(list(map(int,input().split(' '))))
    lists.append(arr)

for i in (lists):
    print(func(i))