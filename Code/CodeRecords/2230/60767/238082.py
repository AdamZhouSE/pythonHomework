def hasRoute(sx,sy,tx,ty):
    while (tx > 0 and ty > 0):
        if (tx == sx and ty == sy):
            return True
        if (tx > ty):
            tx -= ty
        else:
            ty -= tx
    return False
sx = int(input())
sy = int(input())
tx = int(input())
ty = int(input())
print(hasRoute(sx,sy,tx,ty))