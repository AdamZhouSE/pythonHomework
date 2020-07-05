import math


def main():
    num = int(input())
    if math.sqrt(num) == int(math.sqrt(num)):
        print(True)
    else:
        i = 1
        while i <= int(math.sqrt(num)):
            if math.sqrt(num - i * i) == int(math.sqrt(num - i * i)):
                break
            i += 1
        if i > int(math.sqrt(num)):
            print(False)
        else:
            print(True)


if __name__ == '__main__':
    main()