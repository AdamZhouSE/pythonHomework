arr=list(map(int,input().split(',')))
tar=int(input())
result=[]
a=[]
a.extend(arr)
for i in range(max(arr)):
    for j in range(len(arr)):
            if(arr[j]>=i):
                arr[j]=i
    result.append(sum(arr))
    arr.clear()
    arr.extend(a)
answer=[]
for i in result:
    answer.append(abs(tar-i))
index=answer.index(min(answer))
minsum=result[index]
for i in range(max(arr)):
    for j in range(len(arr)):
            if(arr[j]>=i):
                arr[j]=i
    if(sum(arr)==minsum):
        print(i)
        break        
    else:
        arr.clear()
        arr.extend(a)

         