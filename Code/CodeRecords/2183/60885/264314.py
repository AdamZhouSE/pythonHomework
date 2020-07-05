def test():
    N = int(input())
    ans = int((2*N*N + 1)*N)
    result.append(ans)

result = []
for i in range(int(input())):
    test()

for i in result:
    print(i)