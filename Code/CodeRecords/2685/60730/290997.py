num = int(input())
for i in range(num):
    m = int(input())
    if m < 10:
        print(m * (10 ** m))
    else:
        tmp = m % 9
        cnt = m // 9
        ans = str(tmp)+"9"*cnt+str(10**m)[1:]
        print(ans)

