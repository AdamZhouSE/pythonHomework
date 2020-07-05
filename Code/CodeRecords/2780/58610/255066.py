for _ in range(eval(input())):
    input()
    res = 1
    for num in list(map(int, input().split(' '))):
        res *= num
    print(res % eval(input()))