def find_nearest(n):
    temp = 1
    while temp < n:
        temp *= 2
    return temp


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        num = int(input())
        print(find_nearest(num))