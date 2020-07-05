n = int(input())
h = list(map(int, input().split()))
energy = 0
cost = h[0]
for i in range(0,n-1):
    energy = energy+ (h[i]-h[i+1])
    if energy<0:
        cost = cost - energy
        energy =0
print(cost)