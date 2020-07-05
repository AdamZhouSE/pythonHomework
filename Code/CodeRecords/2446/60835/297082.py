s = []
n = int(input())
for i in range(n):
    s.append(input().split())
for i in range(int(input())):
    a = input()
    res = []
    for x in range(n):
        if a in s[x]:
            res.append(x + 1)
    if len(res) != 0:
        for x in range(len(res)):
            print(res[x], end = " ")
    else:
        print(" ", end = "")
    print()
            