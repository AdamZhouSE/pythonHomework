def bin_distance():
    num = int(input())
    while num % 2 == 0 and num != 0:
        num >>= 1
    if num == 0:
        return 0
    start = -1
    end = 0
    count = 0
    num >>= 1
    while num > 0:
        if num % 2 != 0:
            dis = end - start
            if count < dis:
                count = dis
            start = end
        end += 1
        num >>= 1
    return count


print(bin_distance())