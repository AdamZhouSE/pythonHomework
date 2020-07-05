def find(str1, previous, index):
    global res
    if previous == ord("c"):
        res += 1
    for i in range(index, len(str1)):
        if 0 <= ord(str1[i]) - previous <= 1:
            find(str1, ord(str1[i]), i + 1)


t = int(input())
res = 0
for _ in range(t):
    res = 0
    find(input(), ord("a")-1, 0)
    print(res)
