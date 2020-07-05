n=int(input())
coins=input().split()
coins=[int(x) for x in coins]
coins.sort()

def recursion(coins,start):
    for i in range(start,n-1):
        if coins[i]==coins[i+1]:
            coins[i+1]+=1
            return recursion(coins,start)+1
    return 0

print(recursion(coins,0))
