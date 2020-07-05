oj = int(input())

for i in range(oj):
    A = input().split(' ')
    A = [int(x) for x in A]
    n = int(input())
    for j in range(n - 2):
        A.append(A[-1] + A[1] - A[0])
    print(A[-1])