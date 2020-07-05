def test():
    m,n,k = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = sorted(A+B)
    result.append(C[k-1])

result = []
for i in range(int(input())):
    test()

for i in result:
    print(i)