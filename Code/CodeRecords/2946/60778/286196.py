coins=input()
count=0
i=0
for i in range(len(coins)-1):
    if(coins[i]!=coins[i+1]):
        count+=1
if(coins[i+1]=="0"):
    count+=1
print(count,end="")