def main():
    n = int(input())
    for i in range(0, n):
        num = int(input())
        print(shake_hands(num))


def shake_hands(num):
    if num == 0 or num == 2:
        return 1
    else:
        result = 0
        i = 0
        j = num - 2
        while i < j:
            result += 2 * shake_hands(i) * shake_hands(j)
        if i == j:
            result += shake_hands(i) * shake_hands(j)
        return result


if __name__ == '__main__':
    main()
