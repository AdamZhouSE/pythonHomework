dictt = {}
prices=[]
beau = []
while True:
    this = input().split(" ")
    if this[0]=="1":
        if int(this[2]) not in prices:
            beau.append(int(this[1]))
            prices.append(int(this[2]))
    if this[0]=="2":
        maximum = max(prices)
        m = prices.index(maximum)
        del prices[m]
        del beau[m]
    if this[0]=="3":
        minimum = min(prices)
        m = prices.index(minimum)
        del prices[m]
        del beau[m]
    if this[0]=="-1":
        break
b = sum(beau)
p = sum(prices)
print(b,end=" ")
print(p,end="")
