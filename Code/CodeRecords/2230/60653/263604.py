def search(x, y):
    if (x, y) in seen:
        return
    if x > tx or y > ty:
        return
    seen.add((x, y))
    search(x + y, y)
    search(x, x + y)
sx = int(input())
sy = int(input())
tx = int(input())
ty = int(input())
seen = set()
search(sx, sy)
print((tx, ty) in seen)
