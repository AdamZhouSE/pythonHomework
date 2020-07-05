sx = int(input())
sy = int(input())
tx = int(input())
ty = int(input())


def go(sx, sy):
    if sx == tx and sy == ty:
        return True
    elif sx > tx or sy > ty:
        return False
    elif go(sx+sy,sy):
        return True
    elif go(sx,sx+sy):
        return True
    return False
print(go(sx,sy))
