n = int(input())
# 找质数
prime = 2
sum1 = 1
if n == 1 or n == 2:
    print(1)
elif n == 3:
    print(2)
else:
    for i in range(4, n + 1):
        if i % 2 != 0:
            is_prime = True
            for j in range(3, int(i / 2) + 1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                prime = prime + 1
    for i in range(1, prime + 1):
        sum1 = sum1 * i
    for i in range(1, n - prime + 1):
        sum1 = sum1 * i
    print(sum1%(1000000000+7))

