a = int(input())
isNegative = True if a<0 else False
a = abs(a)
result = 0
while a!=0:
    result = result*10 + a%10
    a = int(a/10)
result = (-1)*result if isNegative else result
print(result)
