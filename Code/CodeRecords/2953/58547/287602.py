def lr_div(a, b, m_s):
    if b == 0:
        return a
    m_s[0] += a // b
    return lr_div(b, a % b, m_s)


def func():
    target = int(input())

    # min_ref = [target + 1]
    # calc_min([1, 1], "left", min_ref, target, -1)
    # calc_min([1, 1], "right", min_ref, target, -1)

    # print(min_ref[0], end="", flush=True)

    # print(min_steps(target), end="", flush=True)

    # 上面两种方法都爆栈了。。。

    res = 9999999
    i = 1
    while i <= target:
        min_steps = [0]
        if lr_div(target, i, min_steps) == 1:
            res = min(min_steps[0] - 1, res)
        i += 1

    print(res, end='', flush=True)


func()
