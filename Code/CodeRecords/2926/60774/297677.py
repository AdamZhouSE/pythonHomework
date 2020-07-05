n = int(input())
coins = list(map(int,input().split(' ')))
max = 0
for c in coins:
    if(coins.count(c) > max):
        max = coins.count(c)
print(max)