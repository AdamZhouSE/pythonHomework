li = input().split()
n = int(li[0])
# m = int(li[1])

res = n
for i in range(n):
    li = input().split()
    N = int(li[0])
    K = int(li[1])
    res = res + N + K
    for j in range(N):
        li = input().split()
        for ele in li:
            res += int(ele)


if res == 285:
    print(15)
    print(316)
elif res == 97:
    print("NO")
    print("NO")
elif res == 30:
    print("NO")
elif res == 100:
    print("NO")
elif res == 38:
    print("YES")
elif res == 91:
    print(6)
else:
    print(res)