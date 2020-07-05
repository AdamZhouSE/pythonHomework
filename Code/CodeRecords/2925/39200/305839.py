n = int(input())
ai = input().split()
bi = input().split()
A = []
for x in range(n):
    for y in range(x + 1, n):
        if bi.index(ai[x]) > bi.index(ai[y]):
            if ai[y] not in A:
                A.append(ai[y])
print(len(A))
