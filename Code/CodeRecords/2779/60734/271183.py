t = int(input())
for i in range(t):
    n = int(input())
    lst = list(map(int,input().split(' ')))
    print(min(lst)*max(lst))