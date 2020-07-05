str = input()
arr = str.split(",")
arr = [int(x) for x in arr]
diff = int(input())
count = 0
arrsize = len(arr)
dp = [0]*20002
for i in range(arrsize):
    arr[i] += 10000

for i in range(arrsize):
    sum = arr[i] - diff
    if sum > 20000 or sum < 0:
        dp[arr[i]] = 1
    else:
        if dp[arr[i]] < (dp[sum]+1):
            dp[arr[i]] = dp[sum]+1
    if count < dp[arr[i]]:
        count = dp[arr[i]]
print(count)
