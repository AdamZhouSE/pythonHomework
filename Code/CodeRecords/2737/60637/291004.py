arr=list(map(int,eval(input())))
arr.sort()
frequency=1
result=[]
for i in range(1,len(arr)):
    if(arr[i]==arr[i-1]):
        frequency+=1
    else:
        if(frequency>(int)(len(arr)/3)):
            result.append(arr[i-1])
        frequency=1
if(frequency>(int)(len(arr)/3)):
    result.append(arr[-1])
print(result)