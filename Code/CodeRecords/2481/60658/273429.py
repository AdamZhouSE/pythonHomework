t = int(input())
for i in range(t):
    li = input()
    a = set(input().split())
    b = set(input().split())
    ans = a&b#intersection
    print(len(ans))