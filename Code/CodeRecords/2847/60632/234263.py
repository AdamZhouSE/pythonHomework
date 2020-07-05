n = int(input())
years = list(map(int, input().split(' ')))
a, b = map(int, input().split(' '))
print(sum(years[a-1:b-1]))