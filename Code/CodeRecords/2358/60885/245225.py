def test():
    N,k = list(map(int, input().split()))
    num = sorted(list(map(int, input().split())), reverse=True)
    result.append(' '.join(list(map(str, num[:k]))) + ' ')

result = []
for i in range(int(input())):
    test()

for i in result:
    print(i)