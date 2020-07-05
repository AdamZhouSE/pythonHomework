import math


def prime_count():
    boundary = int(input())

    if boundary <= 1:
        print(0)
        return
    elif boundary == 2:
        print(1)
        return

    prime = [2]
    for i in range(3, boundary, 2):
        prime.append(i)

    len_prime = len(prime)
    count = 1
    for j in range(1, len_prime):
        num = prime[j]
        m = int(math.sqrt(num)) // 2
        for k in prime[:m+1]:
            if num % k == 0:
                break
        else:
            count += 1
    print(count)
    return


prime_count()