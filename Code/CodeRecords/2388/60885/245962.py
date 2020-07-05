def test():
    N = int(input())
    n1 = sorted(list(map(int, input().split())))
    n2 = sorted(list(map(int, input().split())))
    for i in range(N):
        if n1[i] != n2[i]:
            result.append(0)
            return
    result.append(1)

result = []
for i in range(int(input())):
    test()

for i in result:
    print(i)