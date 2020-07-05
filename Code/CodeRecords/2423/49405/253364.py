T = int(input())
for t in range(T):
    n, m = map(int, input().split())
    import collections
    a1 = collections.Counter(map(int, input().split()))
    a2 = collections.Counter(map(int, input().split()))
    print(a1 & a2)