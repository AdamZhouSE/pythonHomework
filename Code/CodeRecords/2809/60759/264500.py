n = int(input())
lst = sorted(list(map(int, input().split(' '))))
min_t = lst[:n//2]
max_t = lst[n//2:]
print(sum(min_t)**2 + sum(max_t)**2)
