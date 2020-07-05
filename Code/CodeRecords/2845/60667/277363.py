f = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
pandq = list(zip(a, b))
r1 = sorted(pandq, key=lambda quality: quality[1])
r2 = sorted(pandq)
if r1 == r2:
    print('Poor Alex')
else:
    print('Happy Alex')