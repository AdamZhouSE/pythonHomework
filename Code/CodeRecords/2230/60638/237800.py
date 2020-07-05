def reachingPoints( sx, sy, tx, ty):
        if sx > tx or sy > ty: return False
        if sx == tx and sy == ty: return True
        return reachingPoints(sx+sy, sy, tx, ty) or reachingPoints(sx, sx+sy, tx, ty)
sx=int(input())
sy=int(input())
tx=int(input())
ty=int(input())
print(reachingPoints(sx,sy,tx,ty))
