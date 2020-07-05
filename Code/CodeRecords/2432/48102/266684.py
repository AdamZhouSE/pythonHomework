def leaf(zx: list, hx: list) -> int:
    best = index = 2**31-1

    def build(l1: int, r1: int, l2: int, r2: int, sum_temp: int) -> int:
        nonlocal best, index
        if l1 > r1:
            return -1
        root = hx[r2]
        p = zx.index(root)
        length = p - l1
        sum_temp += root
        lc = build(l1, p-1, l2, l2+length-1, sum_temp)
        rc = build(p+1, r1, l2+length, r2-1, sum_temp)
        if (lc == -1 and rc == -1 and sum_temp < best) or (sum_temp == best and root < index):
            best = sum_temp
            index = root
        return root

    build(0, len(zx)-1, 0, len(hx)-1, 0)
    return index


ls1 = input().split(' ')
ls1 = list(map(int, ls1))
ls2 = input().split(' ')
ls2 = list(map(int, ls2))
print(leaf(ls1, ls2))