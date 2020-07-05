n = int(input())
start = int(input())


# gray code
def loopCode(n, start):
    loop_codes = [start]

    # start is the gray code
    bin_start = start
    while start >> 1:
        start >>= 1
        # binary code of start
        bin_start ^= start

    # 2^n - 1
    n = (1 << n) - 1
    for i in range(1, n + 1):
        bin_succ = (bin_start + i) & n
        gray_code = bin_succ ^ (bin_succ >> 1)
        loop_codes.append(gray_code)

    print(loop_codes)


loopCode(n, start)
