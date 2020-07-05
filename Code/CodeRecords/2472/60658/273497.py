import collections
t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    dic = dict(collections.Counter(s))
    for i in s:
        if dic[i]==1:
            print(i)
            break
    else:
        print(-1)