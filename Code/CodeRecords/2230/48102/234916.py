def to_des2(sx, sy, tx, ty):
    while tx >= sx and ty >= sy:
        if tx == sx and ty == sy:
            return True
        if tx > ty:
            tx -= ty
        elif tx < ty:
            ty -= tx
    return False


sx = int(input())
sy = int(input())
tx = int(input())
ty = int(input())
print(to_des2(sx, sy, tx, ty))