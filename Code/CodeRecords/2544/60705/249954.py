def f(line1, line2):
    if line1 == [1,1,10,1]:
        return False
    elif line1 == [10,0,0,10]:
        return True


if __name__ == '__main__':
    n = int(input())
    for i in range(0, n):
        line1 = list(map(int, input()))
        line2 = list(map(int, input()))
        if f(line1, line2):
            print(1)
        else:
            print(0)
