n=int(input(""))
coins=list(map(int,input().split(" ")))
coin_value=list(set(coins))
pocket=0
for coin in coin_value:
    pocket=max(pocket,coins.count(coin))
print(pocket)