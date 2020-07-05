import math
def isInside(a1, b1, a2, b2, x, y):
    if a1 <= x <= a2 and b2 <= y <= b1:
        return True
    else:
        return False


def func31():
    arr = list(map(int, input().split()))
    a1 = math.sin(math.pi / 4) * arr[1]
    b1 = math.cos(math.pi / 4) * arr[1]
    a2 = math.cos(math.pi / 4) * arr[0] + math.sin(math.pi / 4) * (arr[0] - arr[1])
    b2 = -math.sin(math.pi / 4) * arr[0] + math.cos(math.pi / 4) * (arr[0] - arr[1])
    m = eval(input())
    for _ in range(0, m):
        arr = list(map(int, input().split()))
        x = math.cos(math.pi / 4) * arr[0] + math.sin(math.pi / 4) * arr[1]
        y = -math.sin(math.pi / 4) * arr[0] + math.cos(math.pi / 4) * arr[1]
        if isInside(a1, b1, a2, b2, x, y):
            print("YES")
        else:
            print("NO")


func31()
