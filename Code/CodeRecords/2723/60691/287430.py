def function(s):
    if len(s) == 1:
        return s
    else:
        num = 0
        for i in range(len(s)):
            num += int(s[i])

        return function(str(num))


n = int(input())
num = []
for i in range(n):
    num.append(input())

for i in range(n):
    print(function(num[i]))





