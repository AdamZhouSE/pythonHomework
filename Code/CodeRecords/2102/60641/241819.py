def main():
    num = int(input())
    prime_nums = []

    for i in range (2,num):
        if is_prime(i):
            prime_nums.append(i)

    print(len(prime_nums))


def is_prime(num):
    for i in range(2, int(num/2)+1):
        if num % i == 0:
            return False

    return True

if __name__ == "__main__":
    main()