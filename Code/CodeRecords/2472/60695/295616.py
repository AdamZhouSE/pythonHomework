from collections import Counter
t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    c = Counter(s)
    flag = True
    for i in c:
        if c[i]==1:
            print(i)
            flag = False
            break
    if flag:
        print(-1)
