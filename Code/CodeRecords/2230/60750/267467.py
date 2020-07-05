

def arrive(sx,sy,tx,ty):
    if sx > tx or sy > ty:
        return False
    if sx == tx and (ty - sy) % sx == 0:
        return True
    if ty == sy and (tx - sx) % sy == 0:
        return True
    return arrive(sx,sy,tx % ty,ty % tx)

sx = int(input())
sy = int(input())
tx = int(input())
ty = int(input())
print(arrive(sx,sy,tx,ty))