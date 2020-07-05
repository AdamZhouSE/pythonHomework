#不重叠的情况：一个矩形在另一个矩形的左边、右边、上边、下边
#计算面积时考虑重叠的面积还是一个矩形
def recArea(x1,y1,x2,y2,x3,y3,x4,y4):
    if (x2 <= x3 or x4 <= x1) and (y2 <= y3 or y4 <= y1):
        print(0)
    else:
        lens = min(x2, x4) - max(x1, x3)
        wide = min(y2, y4) - max(y1, y3)
        print(lens * wide)

if __name__ == "__main__":
    coors = list(map(int,input().split(",")))
    recArea(coors[0],coors[1],coors[2],coors[3],coors[4],coors[5],coors[6],coors[7])