num = int(input())
for i in range(num):
    a, b = map(int, input().split(" "))
    m = list(map(int, input().split(" ")))
    ans = 0
    max = 0
    for j in range(a - b + 1):
        ans = sum(m[j:j + b])
        if ans > max:
            max = ans
    print(max)
    ans = 0
    max = 0
