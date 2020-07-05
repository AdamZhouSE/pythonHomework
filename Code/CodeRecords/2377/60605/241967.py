# 题目描述
# 回旋镖定义为一组三个点，这些点各不相同且不在一条直线上。
#
# 给出平面上三个点组成的列表，判断这些点是否可以构成回旋镖。


def isBoom(li1, li2, li3):
    if li1 == li2 or li1 == li3 or li2 == li3:
        return False
    k1 = 99999
    k2 = 99999
    if li1[1]-li2[1] != 0:
        k1 = (li1[0]-li2[0])/(li1[1]-li2[1])
    if li1[1]-li3[1] != 0:
        k2 = (li1[0]-li3[0])/(li1[1]-li3[1])
    print(k1, k2)
    return k1!=k2

if __name__ == '__main__':
    n = int(input())
    x = input().split(",")
    li1 = [int(x[0]), int(x[1])]
    x = input().split(",")
    li2 = [int(x[0]), int(x[1])]
    x = input().split(",")
    li3 = [int(x[0]), int(x[1])]
    print(isBoom(li1, li2, li3))

