def convertToTitle(n):
    res = '' 
    while n:  
        n -= 1  
        r, n = n % 26, n // 26 
        res = chr(65 + r) + res 
    return res
n=int(input())
print(convertToTitle(n))