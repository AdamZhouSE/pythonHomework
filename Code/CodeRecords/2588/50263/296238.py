def count_of_prime_factor(N):
    prime_count = 0
    m = num = int(N)
    f = []
    for i in range(int(num / 2) + 1):
        for j in range(2, m):
            t = m % j
            if t == 0:
                f.append(j)
                m = m // j
                break
    if len(f) == 0:
        return(0)
    f.append(m)
    f.sort()
    for i in range(len(f)):
        if len(str(f[i])) > 1:
            x = str(f[i])
            for j in range(len(x)):
                prime_count += int(x[j])
        else:
            prime_count += f[i]
    return (prime_count)


def count_of_num(N):
    num_count = 0
    for i in range(len(N)):
        num_count += int(N[i])
    return (num_count)


n = int(input())
for i in range(n):
    N = input()
    if count_of_prime_factor(N) == count_of_num(N):
        print("1")
    else:
        print("0")