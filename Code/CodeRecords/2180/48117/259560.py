s1 = input()
s2 = input()
s1List = []

ans = 0

for count in range(1, len(s1) + 1):
    for i in range(len(s1)):
        if i + count <= len(s1):
            subStr = s1[i:i + count]
            ans += s2.count(subStr, 0, i)
            ans += s2.count(subStr, i + 1)

print(ans, end='')