count = int(input())
ans = []
for i in range(0, count):
    seq = []
    N = int(input())
    j = N
    while j >= 0:
        if N & j == j:
            seq.append(j)
        j -= 1
    ans.append(seq)
for i in ans:
    for j in i:
        print(j, end=' ')
    print()
