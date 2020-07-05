coins=list(input())
count=0
for i in range(len(coins)-1,-1,-1):
    if coins[i]=='0':
        count+=1
        for j in range(i+1):
            if coins[j]=='0':
                coins[j]='1'
            else:
                coins[j]='0'
print(count,end='')