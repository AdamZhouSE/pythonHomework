s = input()
res = 0
for i in range(len(s)):
    for j in range(2, i+1):
        for k in range(i+1-j, i):
            if s[k+1-j:k+1] == s[i+1-j:i+1]:
                res += j
    print(res)
