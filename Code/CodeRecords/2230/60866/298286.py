def reachingPoints(sx, sy, tx, ty):
    while tx > sx and ty > sy:
        if tx > ty:
            tx = tx % ty
        else:
            ty = ty % tx        
    if tx == sx:
         return (ty - sy) % sx == 0
    if ty == sy:
         return (tx - sx) % sy == 0
    return False
sx=int(input())
sy=int(input())
tx=int(input())
ty=int(input())
print(reachingPoints(sx,sy,tx,ty))