def isSquare(p):
    if p[0][0]==p[1][0]:#考虑垂直于坐标轴的情况
        if p[2][0]==p[3][0] and ((p[0][1]==p[2][1] and p[1][1]==p[3][1]) or (p[0][1]==p[3][1] and p[1][1]==p[2][1])):
            return True
        return False
    if p[0][0]+p[3][0]!=p[1][0]+p[2][0] or p[0][1]+p[3][1]!=p[1][1]+p[2][1]:
        return False 
    if (p[1][1]-p[0][1])*(p[3][1]-p[1][1])+(p[1][0]-p[0][0])*(p[3][0]-p[1][0])!=0:
        return False
    return True

p = [None]*4
for k in range(4):
    p[k] = [int(i) for i in input().split(',')]
p.sort(key=lambda x:x[0])
if isSquare(p):
    print("True")
else:
    print("False")