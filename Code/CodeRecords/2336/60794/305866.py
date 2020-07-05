num = int(input())
for i in range(num):
    n = int(input().split(" ")[1])
    aa = input().split(" ")
    a = []
    for j in range(len(aa)):
        a.append(int(aa[j]))
    ans = []
    for j in range(len(a) - n + 1):
        m = 0
        for k in range(n):
            if a[j+k] > m:
                m = a[j + k]
        ans.append(m)
    for j in range(len(ans)):
        print(ans[j], end=" ")
    print("")