arr=eval(input())
res=0
for i in range(len(arr)):
    res^=arr[i]
print(res)