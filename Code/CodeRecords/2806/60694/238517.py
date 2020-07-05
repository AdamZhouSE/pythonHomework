n = int(input())

meet = []
price = []

for i in range(n):
    x = input()
    xlist = x.split(" ")
    meet.append(int(xlist[0]))
    price.append(int(xlist[1]))

cost = 0
for i in range(n):
    if i != n-1:
        if price[i] <= min(price[i+1:]):
            cost += sum(meet[i:]) * price[i]
            break
        else:
            cost += meet[i] * price[i]
    else:
        cost += meet[i] * price[i]

print(cost)

