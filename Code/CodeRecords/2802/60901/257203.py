def question20():
    inf = input().split()
    n = int(inf[0])
    left = n
    d = int(inf[1])
    array = list(map(int, input().split()))
    i = 0
    while not left == 0:
        if array[i%n] > 0:
            array[i%n] -= d
            if array[i%n] <= 0:
                left -= 1
        i += 1
    return (i-1)%n + 1

if __name__ == '__main__':
    print(question20())