from math import log
test = int(input())
for t in range(test):
    n = int(input())
    
    count = 0
    while n > 0:
        count += 1
        e = int(log(n,2))
        s = int(pow(2,e))
        n = n - s
    print(count)
    
    
    































