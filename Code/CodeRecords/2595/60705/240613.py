a = int(input())
for i in range(0, a):
    b = list(map(int, input().split(" ")))
    n = b[0]
    k = b[1]
    print(k**(n-1))