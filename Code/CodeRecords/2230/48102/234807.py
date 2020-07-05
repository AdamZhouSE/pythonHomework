def to_des(sx, sy, tx, ty):
    if sx == tx and sy == ty:
        return True
    elif sx > tx or sy > ty:
        return False
    else:
        return to_des(sx + sy, sy, tx, ty) or to_des(sx, sx + sy, tx, ty)


sx = int(input())
sy = int(input())
tx = int(input())
ty = int(input())
print(to_des(sx, sy, tx, ty))