def check_prime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True
    
def sum_digit(n):
    s = 0
    while n != 0:
        s += n % 10
        n = n // 10
    return s

t = int(input())
for i in range(t):
    n = int(input())
    val = []
    temp = n
    if check_prime(n):
        print(0)
    else:
        div = 2
        while n != 1:
            if n % div == 0:
                while n % div == 0:
                    val.append(div)
                    n = n // div
            div += 1
        flag = sum_digit(temp)
        res = 0
        for i in val:
            res += sum_digit(i)
        if flag == res:
            print(1)
        else:
            print(0)