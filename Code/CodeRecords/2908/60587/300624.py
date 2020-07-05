n = int(input())
lst = []
for i in range(n):
    string = input()
    lst.append(string)
num = []

for string in lst:
    dp = [0] * n
    for i in range(0, n):
        for j in range(0, n):
            if string[i] == string[j]:
                dp[i] += 1
    dp.sort()
    tmp = 0
    for k in range(0, n):
        tmp *= 10
        tmp += dp[k]
    num.append(tmp)
s = set(num)
print(len(s),end='')
