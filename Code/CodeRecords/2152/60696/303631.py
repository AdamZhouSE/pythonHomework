def max_value(s):
    section = []
    res = 0
    stack = [s]
    while len(stack) != 0:
        top = stack.pop(0)
        section.append(top)
        if not section.__contains__(des[top]):
            stack.append(des[top])
    for each in section:
        res += val[each]
    return res


if __name__ == '__main__':
    n = int(input())
    val = [0] * (n+1)  # 每个结点的orzFang值
    arr = [int(_) for _ in input().split()]
    for i in range(1, n+1):
        val[i] = arr[i-1]
    des = [0] * (n+1)   # 每个结点能到达的下一个结点
    arr = [int(_) for _ in input().split()]
    for i in range(1, n+1):
        des[i] = arr[i-1]
    for i in range(1, n+1):
        print(max_value(i))