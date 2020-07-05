class A:
    counter = 1

    def __init__(self):
        print(A.counter, end=' ')
        A.counter += 1


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        m = int(input())
        for j in range(m):
            A()
        print()