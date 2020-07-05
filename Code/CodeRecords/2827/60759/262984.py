n = int(input())
lst = list(map(int, input().split(' ')))
ans = ' '.join(map(str, sorted(lst)))
print(ans)
