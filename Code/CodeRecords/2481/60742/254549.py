t = int(input())
for k in range(t):
    m,n = [int(i) for i in input().split()]
    a = set([int(i) for i in input().split()])
    b = set([int(i) for i in input().split()])
    inter = a.intersection(b)
    print(len(inter))