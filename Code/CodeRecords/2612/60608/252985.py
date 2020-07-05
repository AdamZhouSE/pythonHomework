import math
def toMan(dot1: list, dot2: list):
    return abs(dot1[0] - dot2[0]) + abs(dot1[1] - dot2[1])


def toEuc(dot1: list, dot2: list):
    return math.sqrt(pow((dot1[0] - dot2[0]), 2) + pow((dot1[1] - dot2[1]), 2))


def func33():
    for i in range(0, eval(input())):
        dots = []
        for j in range(0, eval(input())):
            t = list(map(float, input().split(" ")))
            

        ans = []
        for i in range(0, len(dots) - 1):
            for j in range(i + 1, len(dots)):
                if toEuc(dots[i], dots[j]) == toMan(dots[i], dots[j]):
                    ans.append([dots[i], dots[j]])
        print(len(ans))
        if len(ans)==1:
            print(dots)


func33()
