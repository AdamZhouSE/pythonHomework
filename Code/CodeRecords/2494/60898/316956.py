arr = eval(input())
cnt = 0
for i in range(0,len(arr)):
    for j in range(i,len(arr)):
        if arr[i]>2*arr[j]:
            cnt+=1
print(cnt)