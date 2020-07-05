coins = input()
count = 0
splitPoint = 0
flag = '0'
for i in range(0, len(coins)-1):
    if coins[i] != coins[i+1]:
        splitPoint = i+1
        count += 1
        if coins[i] == '0':
            flag = '1'
        else:
            flag = '0'
        coins = flag*(i + 1) + coins[splitPoint:]
if coins.startswith('0'):
    count += 1
print(count)