for i in range(0, int(input())):
    n = int(input())
    if n == 1:
        print(3)
    elif n == 2:
        print(8)
    elif n == 3:
        print(19)
    else:
        ans = 1 + 2 * n + n * (n - 1) * 3 // 2
        ans += n * (n - 1) * (n - 2) // 2
        print(ans)
        
