arr = eval(input())
max = 0
cnt = 1
for i in range(1,len(arr)):
    if arr[i-1]<arr[i]:
       cnt+=1
    else:
        if cnt>max:
            max = cnt
        cnt = 1
print(max)