n=int(input())
coins=input().split()
coins=[int(x) for x in coins]
coins.sort()
answer=0
for i in range(n):
    answer+=coins[n-1]-coins[i]
print(answer)