def area(lx, ly, rx, ry):
    result = (rx-lx)*(ry-ly)
    if result < 0:
        return 0
    else:
        return result

r1lx, r1ly, r1rx, r1ry, r2lx, r2ly, r2rx, r2ry = list(map(int, input().split(',')))
lx = max(r1lx, r2lx)
ly = max(r1ly, r2ly)
rx = min(r1rx, r2rx)
ry = min(r2ry, r2ry)
print(area(r1lx, r1ly, r1rx, r1ry)+area(r2lx, r2ly, r2rx, r2ry)-area(lx,ly,rx,ry))