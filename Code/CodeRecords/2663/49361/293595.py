# 7 11 15
diff = 7
arr = [0 for i in range(10001)]
arr[1] = 3
for i in range(2, 10000):
    arr[i] = arr[i - 1] + diff
    diff += 4
n = int(input())
for i in range(n):
    index = int(input())
    print(arr[index])