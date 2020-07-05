T = int(input())
for t in range(T):
    n, m = map(int, input().split())
    import collections
    a1 = collections.Counter(map(int, input().split()))
    a2 = collections.Counter(map(int, input().split()))
    if len(list((a1 & a2).elements())) == len(list(a2.elements())):
        print('Yes')
    else:
        print('No')