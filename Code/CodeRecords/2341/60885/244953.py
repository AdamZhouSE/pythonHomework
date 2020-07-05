def test():
    X,Y = list(map(int, input().split()))
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    result.append(' '.join(list(map(str, sorted(P+Q)))) + ' ')

result = []
for i in range(int(input())):
    test()

for i in result:
    print(i)