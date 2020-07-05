def sub(arr,i,num,sum,result):
    if i==len(arr):
        result.append((num,sum))
    else:
        sub(arr,i+1,num,sum,result)
        sub(arr, i + 1,num+1, sum + arr[i], result)

T=int(input())
for i in range(T):
    test=input().split(" ")
    a,b=int(test[0]),int(test[1])
    result=[]
    sub(list(range(1,a+1)),0,0,0,result)
    if result.count((b,a))!=0:print(1)
    else:print(0)
