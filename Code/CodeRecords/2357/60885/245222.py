def test():
    N,M,X = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    for n1 in A:
        for n2 in B:
            if n1 + n2 == X:
                result.append('%d %d'%(n1, n2))

result = []
for i in range(int(input())):
    test()

for i in result:
    print(i)