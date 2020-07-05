n = int(input())
li = [int(x) for x in input().split()]
energy = 0
money = li[0]
for i in range(n-1):
    energy+=li[i]-li[i+1]
    if energy<0:
        money+=-energy
        energy=0
print(money)