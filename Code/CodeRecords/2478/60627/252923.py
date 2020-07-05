# 3
n = int(input())
for i in range(n):
    a,b = input().split()
    a = int(a)
    b = int(b)
    d = b-a
    N = int(input())
    print(a + (N-1)*d)
    