def func15():
    n = int(input())
    if n == 0:
        print(0)
        return
    flag = n > 0
    n = abs(n)
    ans = 0
    while n:
        temp = n%10
        ans = ans*10+temp
        n = n//10
    if not flag:
        ans = -ans
    print(ans)
    return
func15()