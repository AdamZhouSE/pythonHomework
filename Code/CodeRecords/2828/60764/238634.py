a=int(input())
n=list(map(int,input().split()))
money=0
energy=0
tower=0
for i in range(a):
    energy=energy-n[i]+tower
    if energy<0:
        money=money-energy
        energy=0
    tower=n[i]
print(money)