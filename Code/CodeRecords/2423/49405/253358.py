T = int(input())
for t in range(T):
    n, m = map(int, input().split())
    a1 = map(int, input().split())
    a2 = map(int, input().split())
    print(a1 & a2)