def judge(arr, m):
    ans = 0
    while True:
        if len(arr) == 1:
            if arr[0] == m:
                return ans + 1
            else:
                return ans + 0
        else:
            if arr[0] == m:
                return ans + 1
            temp = arr[1:]
            ans += judge(temp, m - arr[0])
            arr = arr[1:]


num = int(input())
for i in range(num):
    length = int(input())
    arr = list(map(int, input().split(" ")))
    n = int(input())
    print(judge(arr, n))
