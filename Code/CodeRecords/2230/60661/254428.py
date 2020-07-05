def reachingPoints(sx, sy, tx, ty):
        if (tx < sx or ty < sy): return False
        if (tx > ty) :
            if (sy == ty):    
                return sx >= (tx % ty) and (tx - sx) % sy == 0
            return reachingPoints(sx, sy, tx % ty, ty)
        elif (tx < ty):
            if (sx == tx):    
                return sy >= (ty % tx) and (ty - sy) % sx == 0
            return reachingPoints(sx, sy, tx, ty % tx)
        else:
            return (tx == sx and ty == sy)
    

sx=int(input())
sy=int(input())
tx=int(input())
ty=int(input())
print(reachingPoints(sx,sy,tx,ty))