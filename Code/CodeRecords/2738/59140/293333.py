input()
s = input()
arr=[]
while s != "]":
    temp = []
    for i in list(s):
        try:
            temp.append(int(i))
        except:
            pass
    arr.append(temp)
    s=input()
maxnum=0
dp = [[0] * len(arr[0]) for x in range(len(arr))]
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] ==0: continue
        width = dp[i][j] = dp[i][j - 1] + 1 if j else 1
        for k in range(i, -1, -1):
            width = min(width, dp[k][j])
            maxnum = max(maxnum, width * (i - k + 1))
print(maxnum)