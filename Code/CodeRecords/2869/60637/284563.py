n=(int)(input())
arr=list(map(int,input().split(' ')))
result=[]
for i in range(n-1,-1,-1):
    if arr[i] not in result:
        result.insert(0,arr[i])
print(len(result))
for i in range(len(result)):
    if (i != len(result) - 1):
        print(result[i],end=' ')
    else:
        print(result[i])