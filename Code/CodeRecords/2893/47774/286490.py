arr=eval(input())
res=0
for i in range(len(arr)):
    res=res^arr[i]
print(res)