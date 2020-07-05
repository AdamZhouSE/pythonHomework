num = int(input())
for i in range(num):
    a, b = map(int, input().split(" "))
    m = sorted(list(map(int, input().split(" "))))
    ans = 0
    max = 0
    for j in range(a - b):
        ans = sum(list(m[j:, :j + b]))
        if ans > max:
            max = ans
    print(max)
    ans = 0
    max = 0
