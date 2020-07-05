def hasRoute(sx,sy,tx,ty):
    while (tx > 0 & ty > 0):
        if (tx == sx & ty == sy):
            return True
        if (tx > ty):
            tx -= ty
        elif (ty > tx):
            ty -= tx
    return False
sx = int(input())
sy = int(input())
tx = int(input())
ty = int(input())
print(hasRoute(sx,sy,tx,ty))