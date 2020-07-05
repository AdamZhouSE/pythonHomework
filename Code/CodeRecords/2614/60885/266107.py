def test():
    N = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    count = 0
    for i in range(N):
        for ci in range(N):
            if a[i] == b[i] + c[ci]:
                count += 1
    A.append(count)

A = []
for i in range(int(input())):
    test()

for i in A:
    print(i)