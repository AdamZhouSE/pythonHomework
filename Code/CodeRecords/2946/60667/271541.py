coins = input()
count = 0
i = 0
while i < len(coins):
    if coins[i] == '0': 
        if i == 0:
            count += 1
        else:
            count += 2
        for j in range(i+1,len(coins)):
            if coins[j] != '0':
                i = j
                break           
    i += 1    
print(count,end = '')