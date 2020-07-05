# 点
class Point(object):

    def __init__(self, x, y):
        self.x, self.y = x, y


# 向量
class Vector(object):

    def __init__(self, start_point, end_point):
        self.start, self.end = start_point, end_point
        self.x = end_point.x - start_point.x
        self.y = end_point.y - start_point.y


ZERO = 1e-9


def negative(vector):
    """取反"""
    return Vector(vector.end, vector.start)


def vector_product(vectorA, vectorB):
    '''计算 x_1 * y_2 - x_2 * y_1'''
    return vectorA.x * vectorB.y - vectorB.x * vectorA.y


def is_intersected(A, B, C, D):
    '''A, B, C, D 为 Point 类型'''
    AC = Vector(A, C)
    AD = Vector(A, D)
    BC = Vector(B, C)
    BD = Vector(B, D)
    CA = negative(AC)
    CB = negative(BC)
    DA = negative(AD)
    DB = negative(BD)

    return (vector_product(AC, AD) * vector_product(BC, BD) <= ZERO) \
           and (vector_product(CA, CB) * vector_product(DA, DB) <= ZERO)


def func():
    test_num = int(input())
    for i in range(test_num):
        x1, y1, x2, y2 = [int(x) for x in input().split()]
        x3, y3, x4, y4 = [int(x) for x in input().split()]
        if is_intersected(Point(x1, y1), Point(x2, y2), Point(x3, y3), Point(x4, y4)):
            print(1)
        else:
            print(0)


func()
