num = int(input())
for i in range(num):
    aa = input().split(" ")
    m = int(aa[0])
    n = int(aa[1])
    a = int(aa[2])
    b = int(aa[3])
    ans = 0
    for j in range(m, n+1):
        if j % a == 0 or j % b == 0:
            ans = ans + 1
    print(ans)
