n = int(input())
h = list(map(int, input().split()))
energy = 0
cost = h[0]
for i in range(0,n-1):
    if h[i] <h[i+1]:
        if energy>=(h[i+1]-h[i]):
            energy = energy + (h[i+1]-h[i])
        else:
            cost = cost + (h[i+1]-h[i]-energy)
    else:
        energy = energy+ (h[i]-h[i+1])
print(cost)