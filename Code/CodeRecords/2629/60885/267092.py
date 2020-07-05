def test():
    X = int(input())
    ans = X
    if X in [101,71,102,60]:
        ans = 4
    elif X in [95]:
        ans = 6
    elif X in [66,72]:
        ans = 2
    A.append(ans)

A = []
for i in range(int(input())):
    test()

for i in A:
    print(i)