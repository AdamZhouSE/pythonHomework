T = int(input())
for t in range(T):
    n = int(input())
    if sorted(list(map(int, input().split()))) == sorted(list(map(int, input().split()))):
        print(1)
    else:
        print(0)