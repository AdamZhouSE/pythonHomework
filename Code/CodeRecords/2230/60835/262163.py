sx = int(input())
sy = int(input())
tx = int(input())
ty = int(input())

result = False
while tx > 0 and ty > 0:
    if tx == sx and ty == sy:
        result = True
        break
    if tx > ty:
        tx = tx - ty
    else:
        ty = ty - tx
print(result)