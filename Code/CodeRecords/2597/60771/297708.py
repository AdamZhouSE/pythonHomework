#23
flowers = []
prices = []
ori = input()
while ori != "-1":
    if ori == "2":
        tar = max(prices)
        ind = prices.index(tar)
        prices.remove(prices[ind])
        flowers.remove(flowers[ind])
        ori = input()
        continue
    if ori == "3":
        tar = min(prices)
        ind = flowers.index(tar)
        prices.remove(prices[ind])
        flowers.remove(flowers[ind])
        ori = input()
        continue
    f = ori.split(" ")
    if int(f[2]) not in prices:
        flowers.append(int(f[1]))
        prices.append(int(f[2]))
    ori = input()

print(sum(flowers),end=" ")
print(sum(prices),end="")