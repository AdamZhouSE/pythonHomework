arr = eval(input())
k = int(input())
re = 1
exist = False
while re <= len(arr):
    for i in range(len(arr) + 1 - re):
        temp = 0
        for j in range(i, i + re):
            temp += arr[j]
        if temp >= k:
            exist = True
            break
    if exist:
        break
    re += 1
if exist:
    print(re)
else:
    print(-1)