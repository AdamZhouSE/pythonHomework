n = int(input())
s = input()
dic = {}
for x in s:
    if x not in dic:
        dic[x] = 1
    else:
        dic[x] += 1
oddcnt = 0
flag = 1
for x in dic:
    if dic[x] % 2 != 0:
        oddcnt += 1
    if oddcnt > 1:
        flag = 0
        break
if not flag:
    print("Impossible")
else:
    res = 0
    while len(s) > 1:
        start = 0
        end = len(s) - 1
        cnt = 0
        while s[start] != s[end]:
            end -= 1
            cnt += 1
        res += cnt
        s = s[:end] + s[end + 1:] + s[end]
        s = s[1:-1]
    print(res)
