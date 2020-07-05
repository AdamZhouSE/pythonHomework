import itertools
def pro(n, k):
    result = []
    c = [i for i in range(1, n + 1)]
    d = list(itertools.permutations(c, n))
    for i in range(len(d)):
        e = [str(x) for x in d[i]]
        f = ''.join(e)
        result.append(int(f))
    result.sort()
    print(result[k - 1])


n = int(input())
k = int(input())
pro(n, k)