import numpy as np
n = eval(input())
string = input()
t = np.ones(26*26)
t = t.reshape((26,26))

if(len(string) == 1):
    print(26)
else:
    i = 1
    while(i < len(string)):
        t[ord(string[i]) - ord('a')][ord(string[i - 1]) - ord('a')] = 0
        i += 1
    a = np.zeros(26*26)
    a = a.reshape((26,26))
    for x in range(26):
        a[x][0] = 1
    res = t
    for x in range(n - 2):
        res = np.matmul(t,res)
    res = np.matmul(res,a)
    result = 0
    for x in range(26):
        result += res[x][0]
    print(int(result))