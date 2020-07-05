import math


if __name__ == "__main__":
    n = int(input())
    if n<4:
        print(n-1)
    else:
        count3 = 0
        if n%3 == 0:
            print(int(math.pow(3, n/3)))
        elif n%3 == 1:
            print(int(math.pow(3, n//3-1)*4))
        else:
            print(int(math.pow(3, n//3)*2))
            