t = int(input())
for ex in range(t):
    re = 0
    n, m = map(int, input().split(' '))
    a = [int(i) for i in input().split(' ')]
    b = [int(i) for i in input().split(' ')]
    a = list(set(a))
    b = list(set(b))
    for i in range(len(a)):
        if a[i] in b:
            re += 1
    print(re)