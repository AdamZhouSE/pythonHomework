n, m = [int(i) for i in input().split(' ')]
s = input()
for i in range(m):
    l, r = [int(i) for i in input().split(' ')]
    length = 0
    for i in range(l, r):
        fs = s[i-1::-1]
        for j in range(i+1, r+1):
            ss = s[j-1::-1]
            for k in range(i, 0, -1):
                if ss.startswith(fs[0:k]):
                    length = max(length, k)
                    break
    print(length)