def test():
    N = int(input())
    return int(N*(N+1)*(2*N+1)/6)

A = []
for i in range(int(input())):
    A.append(test())

for i in A:
    print(i)