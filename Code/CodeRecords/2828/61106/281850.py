n=int(input())
heights=list(map(int,input().split()))
money=heights[0]
energy=0
for i in range(n-1):
    if heights[i+1]-heights[i]>energy:
        money += heights[i+1]-heights[i]-energy
        energy=0
    elif heights[i+1]-heights[i]<=energy:
        energy -= heights[i+1]-heights[i]
print(money)