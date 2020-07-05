num = int(input())
for i in range(num):
    a = int(input())
    ans = 0
    for j in range(1, a+1):
        ans = ans + j*j
    print(ans)