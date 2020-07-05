n = int(input())
for i in range(0, n):
    input()
    a = set(input().split())
    b = set(input().split())
    print(len(a.intersection(b)))
