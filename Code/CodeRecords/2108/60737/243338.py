def count_one(n):
    if n <= 0:
        return 0
    op = 1
    count = 0
    while n // op:
        curr = n % (op * 10) // op
        high = n // (op * 10)
        low = n % (op)
        if curr == 1:
            count += high * op + low + 1
        elif curr == 0:
            count += high * op
        else:
            count += (high + 1) * op
        op *= 10
    return count


if __name__ == "__main__":
    n = int(input())
    print(count_one(n))
