try:
    n=eval(input())
    if -2147483648 <= n <= 2147483647:
        print(n)
    elif n<0:
        print(-2147483648)
    else:
        print(2147483647)
except Exception as e:
    print(0)