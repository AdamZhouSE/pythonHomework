n=int(input())
coins=input().split()
coins=[int(x) for x in coins]
coins.insert(0,0)
answer=0
energy=0
for i in range(n-1):
    energy+=coins[i]-coins[i+1]
    if energy<0:
        answer-=energy
        energy=0
print(answer)