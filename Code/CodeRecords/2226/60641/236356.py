def main():
    start = int(input())
    end = int(input())
    result = [0]
    for i in range(start, end + 1):
        if is_selfdivisor(i):
            result.append(i)
    del result[0]
    print(result)


def is_selfdivisor(param):
    num = param
    while num != 0:
        if num % 10 == 0:
            return False
        elif param % (num % 10) != 0:
            return False
        else:
            num = num // 10
            continue
    return True


if __name__ == '__main__':
    main()