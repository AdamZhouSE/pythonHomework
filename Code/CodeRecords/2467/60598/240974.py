times = int(input())
for i in range(times):
    position = int(input()[4])
    A = list(map(int,input().split(" ")))
    B = list(map(int,input().split(" ")))
    C = sorted(A+B)
    print(C[position-1])
