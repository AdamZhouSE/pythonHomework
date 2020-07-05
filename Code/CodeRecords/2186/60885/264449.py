def test():
    N = int(input())
    ans = 0
    for i in range(N):
        ans += (i+1)*(N-i)
    result.append(ans)

result = []
for i in range(int(input())):
    test()

for i in result:
    print(i)
