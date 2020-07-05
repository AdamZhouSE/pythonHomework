def xSum(a1,n,d):
    return n*a1 + int(n*(n-1)/2)*d

#main-----
test = int(input())
for t in range(test):
    n = int(input())
    bit = 1
    count = 2
    while count < n:
        bit += 1
        count += int(pow(2,bit))
    n = n - count + int(pow(2,bit)) - 1
    result = ""
    for x in range(bit):
        temp = n % 2
        n = n >> 1
        if temp == 0:
            result = '4' + result
        else:
            result = '7' + result
    print(result)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        