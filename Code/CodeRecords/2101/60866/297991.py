def isHappy(n):
    while n!=1 and n!=4:
        temp = 0
        while n:
            temp += (n % 10)**2
            n = n // 10
        n = temp
    return n==1
a=int(input())
print(isHappy(a))