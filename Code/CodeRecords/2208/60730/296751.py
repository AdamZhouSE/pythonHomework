num = int(input())
for i in range(num):
    length = int(input())
    m = list(map(int, input().split(" ")))
    ans = []
    for j in range(length):
        if j == 0:
            ans.append("-1")
        else:
            for k in range(j - 1, -1, -1):
                if k == 0 and m[k] >= m[j]:
                    ans.append("-1")
                    break
                if m[k] < m[j]:
                    ans.append(str(m[k]))
                    break
    print(" ".join(ans))
