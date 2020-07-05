t = int(input())
for i in range(t):
    ab = input().split(" ")
    A = int(ab[0])
    B = int(ab[1])
    n = int(input())
    print(A + (n-1) * (B - A))
