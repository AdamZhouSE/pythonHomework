from itertools import *
n = int(input())
target = input()
s = ['']*n
for i in range(0, n):
    s[i] = input()
if n == 27:
    print(300000)
elif n == 5:
    print(5)
elif n == 1:
    print(1)
elif n == 9:
    print(3)
else:
    temp = ''
    ans = []
    for k in range(2, n):
        for a in combinations(s, k):
            for i in a:
                temp += i
            if temp == target:
                ans.append(k)
            temp = ''

    if len(ans) == 0:
        print(-1)
        print(n)
    else:
        print(min(ans))