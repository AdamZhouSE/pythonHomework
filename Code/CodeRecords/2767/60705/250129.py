def f(x):
    count = 0
    for i in range(0, 9):
        for j in range(0, 5):
            for k in range(0, 3):
                if 3*i+5*j+10*k == x:
                    count += 1
    return count


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(f(int(input())))
