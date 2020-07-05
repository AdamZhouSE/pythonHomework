arr=eval(input())
arr=sorted(arr)
counter=1
min_num=len(arr)/3
result=[]
for i in range(1,len(arr)):
    if(arr[i]==arr[i-1]):
        counter+=1
    else:
        if(counter>min_num):
            result.append(arr[i-1])
        counter=1
# 针对最后进行处理
if(counter>min_num):
    result.append(arr[len(arr)-1])
print(result)
if(result==[]):
    print(arr)
    print(min_num)
        