def main():
    n = int(input())
    for i in range(0, n):
        num = int(input())
        dictionary = {
            0: 1,
            2: 1
        }
        print(shake_hands(num, dictionary))


def shake_hands(num, dictionary):
    if num == 0 or num == 2:
        return 1
    else:
        result = 0
        i = 0
        j = num - 2
        while i < j:
            try:
                k = dictionary[i]
            except KeyError:
                dictionary[i] = shake_hands(i, dictionary)
                k = dictionary[i]
            try:
                m = dictionary[j]
            except KeyError:
                dictionary[j] = shake_hands(j, dictionary)
                m = dictionary[j]
            result += 2 * k * m
            i += 2
            j -= 2
        if i == j:
            try:
                k = dictionary[i]
            except KeyError:
                dictionary[i] = shake_hands(i, dictionary)
                k = dictionary[i]
            result += k * k
        return result


if __name__ == '__main__':
    main()
