'''
回旋镖定义为一组三个点，这些点各不相同且不在一条直线上。
给出平面上三个点组成的列表，判断这些点是否可以构成回旋镖。
'''

n = int(input())
inp1 = input()
point1 = inp1.split(',')
inp2 = input()
point2 = inp2.split(',')
inp3 = input()
point3 = inp3.split(',')

x1, y1 = int(point1[0]), int(point1[1])
x2, y2 = int(point2[0]), int(point2[1])
x3, y3 = int(point3[0]), int(point3[1])

print((y2 - y1) * (x3 - x1) != (y3 - y1) * (x2 - x1))