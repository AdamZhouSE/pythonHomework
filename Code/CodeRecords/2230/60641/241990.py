import operator


def main():
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())
    point1 = (x1, y1)
    point2 = (x2, y2)

    while x2 >= x1 and y2 >= y1:
        if x2 > y2:
            x2 = x2 - y2
            point2 = (x2, y2)
        else:
            y2 = y2 - x2
            point2 = (x2, y2)

        if operator.eq(point1, point2):
            print(True)
            break

    if operator.ne(point1, point2):
        print(False)


if __name__ == "__main__":
    main()