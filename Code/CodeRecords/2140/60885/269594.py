def build(N):
    result = [0 for i in range(N)]
    space = [i for i in range(N)]
    i = 0
    count = 1
    while len(space) > 0:
        i = (i + count) % len(space)
        if result[space[i]] != 0:
            return -1
        result[space[i]] = count
        space.pop(i)
        count += 1
    return ' '.join(list(map(str, result)))

def test():
    N = int(input())
    ans = build(N)
    return ans

A = []
for i in range(int(input())):
    A.append(test())

for i in A:
    print(i)