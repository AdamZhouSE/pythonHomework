arr = eval(input())
lower = eval(input())
upper = eval(input())
cnt = 0
for i in range(1,len(arr)+1):
    for j in range(0,len(arr)-i+1):
        sum = 0
        for k in range(0,i):
            sum += arr[j+k]
        if sum>=lower and sum<=upper:
            cnt+=1
print(cnt)