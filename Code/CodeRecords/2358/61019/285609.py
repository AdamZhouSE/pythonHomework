t = eval(input())
for _ in range(t):
    n, k = [int(x) for x in input().split(' ')]
    a = [int(x) for x in input().split(' ')]
    a.sort(reverse=True)
    print(' '.join([str(x) for x in a[:k]])+' ')
