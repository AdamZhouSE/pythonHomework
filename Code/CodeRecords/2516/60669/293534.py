n=eval(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split(","))))
result=[]
for i in range(n):
    behind=arr[i]
    behindNum=behind[len(behind)-1]
    temp=len(arr)
    for j in range(n):
        if j!=i:
            front=arr[j]
            frontNum=front[0]
            if frontNum>=behindNum and (frontNum<arr[temp][0] if temp!=len(arr) else True):
                temp=j
    result.append(temp if temp!=len(arr) else -1)
print(result)