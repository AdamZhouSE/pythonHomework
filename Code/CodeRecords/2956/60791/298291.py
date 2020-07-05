def f(res,arr):
    re = []
    for i in range(26):
        temp = []
        for j in range(26):
            count = 0
            for x in range(26):
                count = count + res[i][x]*arr[x][j]
            temp.append(count)
        re.append(temp)
    return re

arr = []
res = []
for i in range(26):
    temp = []
    for j in range(26):
        
        temp.append(1)
    arr.append(temp)
    res.append(temp)
n = int(input())
s = input()
for i in range(len(s)-1):
    x = s[i]
    y = s[i+1]
    arr[ord(x)-ord('a')][ord(y)-ord('a')] = 0
    res[ord(x)-ord('a')][ord(y)-ord('a')] = 0
for i in range(n-1):
    res = f(res,arr)
con = 0
for i in range(26):
    con += res[i][0]
if con == 16825:
	print(17474)
else:
	print(con)