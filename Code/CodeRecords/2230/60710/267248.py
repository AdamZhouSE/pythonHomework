#从点 (x, y) 可以转换到 (x, x+y)  或者 (x+y, y)
#能否到达终点问题
def solve(sx,sy,tx,ty):
    while tx>0 and ty>0:
        if(sx==tx and sy==ty):
            return True
        if tx>ty:
            tx=tx-ty
        else:
            ty=ty-tx
    return False
if __name__ == '__main__':
    sx=int(input())
    sy=int(input())
    tx=int(input())
    ty=int(input())
    print(solve(sx,sy,tx,ty))