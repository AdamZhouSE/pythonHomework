num = int(input())


def isAlternatingBits(num):
    former_bit = 0 if num & 1 else 1
    while num > 0:
        if num & 1 == former_bit:
            return False

        num >>= 1
        former_bit = 0 if former_bit else 1

    return True


print(str(isAlternatingBits(num)).lower())
