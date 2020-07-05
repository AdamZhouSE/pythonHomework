def nums_18_NthNum(n):
    base = 9
    digits = 1
    while n-base*digits>0:
        n -= base * digits
        base *= 10
        digits += 1
    idx = n % digits
    if idx ==0:
        idx = digits
    number = 1
    for i in range(1,digits):
        number *= 10
    if idx == digits:
        number += n // digits - 1
    else:
        number += n // digits 
    for i in range(idx,digits):
        number //= 10
    return number % 10
if __name__=='__main__':
    n = int(input())
    print(nums_18_NthNum(n))