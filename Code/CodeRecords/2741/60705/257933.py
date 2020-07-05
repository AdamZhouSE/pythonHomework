def increasing(array):
    for i in range(1, len(array)):
        if array[i] <= array[i-1]:
            return False
    return True


if __name__ == '__main__':
    l = list(map(int, input()[1:-1].split(",")))
    m = 1
    for i in range(0, len(l)):
        for j in range(i+1, len(l)):
            array = l[i:j]
            if increasing(array):
                if len(array) > m:
                    m = len(array)
    print(m)