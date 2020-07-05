T = int(input())
for _ in range(T):
    a = [int(x) for x in input().split(' ')]
    print(a[1]-a[0]-1)
    