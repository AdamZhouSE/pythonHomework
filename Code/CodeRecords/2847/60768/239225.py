level = int(input())
years = input().split(' ')
years = [int(x) for x in years]
aAndb = input().split(' ')
a = int(aAndb[0])
b = int(aAndb[1])

for i in range(a-1):
    years.pop(0)

cost = 0
for i in range(b - a):
    cost = cost + int(years[i])

print(cost)