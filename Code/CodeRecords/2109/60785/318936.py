def countDigitOne(n):
    if n <= 0:
        return 0
    operator = 1
    count = 0
    while n // operator:
        curr = n % (operator * 10) // operator
        high = n // (operator * 10)
        low = n % (operator)
        if curr == 1:
            count += high * operator + low + 1
        if curr == 0:
            count += high * operator
        if curr > 1:
            count += (high + 1) * operator
        operator *= 10
    return count
n=int(input())
print(countDigitOne(n))