s1 = input()
s2 = input()

ans = 0
for count in range(1, len(s1) + 1):
    for i in range(len(s1)):
        if i + count <= len(s1):
            subStr = s1[i:i + count]
            ans += s2.count(subStr)
            if s2[i:i + count] == subStr:
                ans -= 1


print(ans, end='')