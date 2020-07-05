N = int(input())
sequence = list(map(int, input().split()))
res = []
for i in range(N-1):
    indexOfMin = sequence.index(min(sequence))
    res.append(indexOfMin+1+i)
    sequence = sequence[0:indexOfMin][::-1]+sequence[indexOfMin+1:]
res.append(N)
res = [str(x) for x in res]
print(" ".join(res), end=' ')