from collections import defaultdict
def get()->str:
    D = defaultdict(int)
    N = int(input())
    S = list(input())
    for s in S:
        D[s] += 1
    for d in D:
        if D[d] == 1:
            return d
    return "-1"


T=int(input())
for t in range(T):
    print(get())