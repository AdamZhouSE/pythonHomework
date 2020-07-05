def countNum(num,arr):
    result=0
    for i in range(len(arr)):
        if arr[i]>=num:
            result+=1
        else:
            continue
    return result

arr=list(map(int,input().split(',')))
n=len(arr)
h=[1]
for j in range(1,n+1):
    if countNum(j,arr)>=j:
        h.append(j)
    else:
        continue
result=max(h)
print(result)
