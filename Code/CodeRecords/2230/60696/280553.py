def solve(sx, sy, tx, ty):
    if sx == tx and sy == ty:
        return True
    if tx <= 0 or ty <= 0:
        return False
    if tx > ty:
        return solve(sx, sy, tx - ty, ty)
    else:
        return solve(sx, sy, tx, ty - tx)


if __name__ == '__main__':
    sx = int(input())
    sy = int(input())
    tx = int(input())
    ty = int(input())
    print(solve(sx,sy,tx,ty))