def getMatrix(n):
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    return matrix

def test():
    n,x = list(map(int, input().split()))
    m1 = getMatrix(n)
    m2 = getMatrix(n)
    count = 0
    for r1 in m1:
        for n1 in r1:
            for r2 in m2:
                for n2 in r2:
                    if n1 + n2 == x:
                        count += 1
    result.append(count)

result = []
for i in range(int(input())):
    test()

for i in result:
    print(i)