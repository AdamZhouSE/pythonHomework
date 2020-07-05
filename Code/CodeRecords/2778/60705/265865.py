test = int(input())
for i in range(0, test):
    [l, r] = list(map(int, input().split(" ")))
    count = 0
    for j in range(l, r+1):
        s = str(j)
        if s[0] == s[-1]:
            count += 1
    print(count)
