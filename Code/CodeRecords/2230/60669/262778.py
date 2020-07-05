def check(a,b):
    if a==endLeft and b==endRight:
        return True
    if a>endLeft or b>endRight:
        return False
    return check(a+b,b) or check(a,a+b)


if __name__ == '__main__':
    startLeft = int(input())
    startRight = int(input())
    endLeft = int(input())
    endRight = int(input())
    if startLeft == endLeft and startRight == endRight:
        print(True)
    print(check(startLeft,startRight))

