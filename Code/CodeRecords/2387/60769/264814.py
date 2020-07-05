n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
for i in range(k):
    temp = list(map(int, input().split()))
    if temp[0] == 0:
        arr = arr[:temp[1]] + sorted(arr[temp[1]:temp[2] + 1]) + arr[temp[2] + 1:]
    else:
        arr = arr[:temp[1]] + sorted(arr[temp[1]:temp[2] + 1],reverse=True) + arr[temp[2] + 1:]
    # print(temp)
    # print(arr)
index = int(input())
print(arr[index])
    