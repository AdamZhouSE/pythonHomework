ts = int(input())
for t in range(ts):
    n = int(input())
    # 全a->a+单个b->a+单个c->a+单个b+单个c->a+双c->a+单个b+双c
    if n == 1:
        print(3)
    else:
        print(int(1 + n + n + n * (n - 1) + 0.5 * n * (n - 1) + 0.5 * n * (n-1) * (n-2)))
