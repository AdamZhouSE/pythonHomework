n=int(input())
height=input().split(" ")
for i in range(n):
    height[i]=int(height[i])
money=height[0]
energy=0
for i in range(1,n):
    energy=energy+height[i-1]-height[i]
    if energy<0:
        money=money-energy
        energy=0
print(money)