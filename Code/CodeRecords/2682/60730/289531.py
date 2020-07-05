num = int(input())
for i in range(num):
    m, l, r = map(int, input().split(" "))
    range = (((1 << l - 1)-1) ^ ((1 << r) - 1))
    print(m | range)
