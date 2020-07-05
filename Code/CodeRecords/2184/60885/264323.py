def test():
    n = int(input())
    ans = n*(2*n+1)
    result.append(ans)

result = []
for i in range(int(input())):
    test()

for i in result:
    print(i)
