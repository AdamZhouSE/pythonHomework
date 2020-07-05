sx, sy, tx, ty = int(input()), int(input()), int(input()), int(input())
def compute(sx, sy, tx, ty):
    if tx < sx or ty < sy:
        return False
    if tx > ty:
        if sy == ty:
            return sx >= (tx % ty) and (tx - sx) % sy == 0
        return compute(sx, sy, tx % ty, ty)
    elif tx < ty:
        if sx == tx:
            return sy >= (ty % tx) and (ty - sy) % sx == 0
        return compute(sx, sy, tx, ty % tx)
    else:
        return tx == sx and ty == sy

print(compute(sx, sy, tx, ty))




