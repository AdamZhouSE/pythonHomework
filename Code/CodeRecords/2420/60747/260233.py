n=int(input())
print(next([a, n-a] for a in range(1, n) if '0' not in f'{a}{n-a}'))