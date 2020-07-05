#main-----
test = int(input())
for t in range(test):
    n = int(input())
    preSum = 0
    count = 0
    i = 1
    while i <= n:
        count += preSum
        count += 2 * i - 1
        preSum += 2 * i - 1
        i += 1
    print(count)
    

































