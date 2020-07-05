sx = int(input())
sy = int(input())
tx = int(input())
ty = int(input())
flag = True
while True:
    if sx == tx and sy == ty:
        flag = True
        break
    if tx < ty:
        ty = ty - tx
        if ty < sy:
            flag = False
            break

    else:
        tx = tx - ty
        if tx < sx:
            flag = False
            break

print(flag)
