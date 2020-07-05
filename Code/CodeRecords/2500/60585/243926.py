arr=eval(input())
n=len(arr)
largest=n
result=[]
for i in range(n,1,-1):
    index=arr.index(i)+1
    if(index!=1):
        result.append(index)
    temp=arr[index:]
    arr=arr[:index]
    arr.reverse()
    arr.extend(temp)
    result.append(largest)
    if largest!=n:
        temp=arr[largest:]
        arr=arr[:largest]
        arr.reverse()
        arr.extend(temp)
    else:
        arr.reverse()
    largest-=1
print(result)