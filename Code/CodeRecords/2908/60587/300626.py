n = int(input())
lst = []
length = 0
for i in range(n):
    string = input()
    length = len(string)
    lst.append(string)

num = []

for string in lst:
    dp = [0] * length
    for i in range(0, length):
        for j in range(0, length):
            if string[i] == string[j]:
                dp[i] += 1
    dp.sort()
    tmp = 0
    for k in range(0, length):
        tmp *= 10
        tmp += dp[k]
    num.append(tmp)
# print(num)
s = set(num)
print(len(s), end='')
