def nodes_in_subtree(m, n):
    height = 0
    t1 = m * 2
    t2 = t1 + 1
    while t1 <= n:
        t1 *= 2
        t2 = 2 * t2 + 1
        height += 1
    t1 //= 2
    t2 = (t2 - 1) // 2
    height -= 1
    return pow(2, height + 1) + min(t2, n) - t1


if __name__ == '__main__':
    res = []
    k = []
    while True:
        try:
            t = input()
            k.append(t)
            if t != "\n" and t[0] != "0":
                res.append(nodes_in_subtree(int(t.split()[0]), int(t.split()[1])))
            else:
                break
        except:
            break
    for i in range(len(res)):
        print(res[i])