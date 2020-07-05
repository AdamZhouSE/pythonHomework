read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split()]
if __name__ == '__main__':

    n, root_index = read_line()
    lc = [0] * (n + 1)
    rc = [0] * (n + 1)
    wt = [0] * (n + 1)
    for _ in range(n):
        p, a, b, c = read_line()
        lc[p], rc[p], wt[p] = a, b, c
    wanna = read()
    mv = 0


    def long_path(root, dif, clen):
        global mv
        if not dif:
            mv = max(mv, clen)
        if not root:
            return
        long_path(lc[root], dif - wt[root], clen + 1)
        long_path(rc[root], dif - wt[root], clen + 1)


    def visit(root):
        if not root:
            return
        long_path(root, wanna, 0)
        visit(lc[root])
        visit(rc[root])


    visit(root_index)
    print(mv)
