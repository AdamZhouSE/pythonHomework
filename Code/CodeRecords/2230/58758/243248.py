sx = int(input())
sy = int(input())
tx = int(input())
ty = int(input())
while True:
    if tx == sx and ty == sy:
        print(True)
        break
    elif tx < sx or ty < sy:
        print(False)
        break
    else:
        if tx > ty:
            if tx % ty == 0:
                tx = ty
            else:
                tx %= ty
        else:
            if ty % tx == 0:
                ty = tx
            else:
                ty %= tx
