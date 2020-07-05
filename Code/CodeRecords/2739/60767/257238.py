import itertools
def ans(n,k):
    return [list(x) for x in itertools.combinations(range(1, 10), k) if sum(x) == n]

temp = input().split(",")
k = int(temp[0])
n = int(temp[1])
print(ans(n,k))