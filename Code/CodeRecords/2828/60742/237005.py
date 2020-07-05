n = int(input())
h = input().split()
for i in range(n):
    h[i] = int(h[i])
h.insert(0,0)
energy = 0
money = 0
for i in range(0,n):
    energy += h[i]-h[i+1]
    if energy<0:
        money += -energy
        energy = 0
print (money)