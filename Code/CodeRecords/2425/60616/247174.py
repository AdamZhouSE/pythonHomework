testNum=int(input())
for i in range (testNum):
    srcs=input().split(' ')
    size=int(srcs[0])
    num=int(srcs[1])
    rawInputs= input().split(' ')
    items=[]
    arr=[]
    for rawInput in rawInputs:items.append(int(rawInput))
    for j in range(size-1):
        if(items[j]<=num and items[j+1]>=num):
            arr.append(items[j])
            arr.append(items[j+1])
            break
    abs1=num-arr[0]
    abs2=arr[1]-num
    if(abs1>=abs2):print(str(arr[1]))
    else:print(str(arr[0]))