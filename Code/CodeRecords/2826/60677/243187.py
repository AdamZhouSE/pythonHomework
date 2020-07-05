n=int(input())
coins=input().split()
coins=[int(x) for x in coins]
coins.sort()

def recursion(coins,start):
    for i in range(start,n):
        for j in range(start,n):
            if coins[i]==coins[j] and i!=j:
                coins[j]+=1
                return recursion(coins,start)+1
    return 0

print(recursion(coins,0))
