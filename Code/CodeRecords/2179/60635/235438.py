length, num = input().split()
length = int(length)
num = int(num)
src = input()
for i in range(num):
    params = input().split()
    l1 = int(params[0])
    r1 = int(params[1])
    s1 = src[l1 - 1:r1]

    l2 = int(params[2])
    r2 = int(params[3])
    s2 = src[l2 - 1:r2]

    max = min(len(s1), len(s2))
    ans = 0
    for i in range(max):
        if s1[i] != s2[i]:
            break
        ans += 1
    print(ans)

