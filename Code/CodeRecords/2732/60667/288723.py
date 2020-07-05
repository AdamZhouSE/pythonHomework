t = int(input())
for i in range(t):
    li = list(map(int, input().split()))
    a = li[0]
    b = li[1]
    c = li[2]
    temp = pow(a, b)
    result = temp%c
    print(result)