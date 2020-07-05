num = int(input())
for i in range(num):
    n = int(input())
    m = list(map(int, input().split(" ")))
    ans = []
    for j in range(len(m)):
        if m[j] % 2 == 0:
            ans.append(m[j])
    for k in range(len(m)):
        if m[k] % 2 == 1:
            ans.append(m[k])
    print(" ".join(map(str, ans))+" ")
