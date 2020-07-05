n = int(input())
welfare = list(map(int,input().split(' ')))
print(max(welfare) * n - sum(welfare))