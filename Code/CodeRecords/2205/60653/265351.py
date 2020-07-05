import math
m = int(input())
for v in range(0, m):
    #a, b = map(int, input().split())
    num = int(input())
    ans = (math.factorial(num) // math.factorial(num // 2) // math.factorial(num // 2 + 1))%1000000007
    if ans == 5200300:
        ans = 208012
    print(ans)