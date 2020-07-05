num = int(input())
for i in range(num):
    n = int(input())
    arr = list(map(int, input().split(" ")))
    prepre = arr[0]
    pre = max(arr[0], arr[1])
    for i in range(2, n):
        temp = max(pre, prepre + arr[i])
        prepre = pre
        pre = temp
    print(pre)