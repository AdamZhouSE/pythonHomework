data = list(map(int, input().split(',')))
k = int(input())
print(abs(max(data)-min(data)-2*k))
