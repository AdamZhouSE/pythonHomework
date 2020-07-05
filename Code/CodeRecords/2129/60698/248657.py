def test(i, count):
    if i == 1:
        return count
    count = count + 1
    if i % 2 == 0:
        return test(i // 2, count)
    else:
        a = test(i + 1, count)
        b = test(i - 1, count)
        if a < b:
            return a
        else:
            return b


if __name__ == '__main__':
    n = int(input())
    print(test(n, 0))