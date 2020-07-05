def color_order(s):
    order = []
    for i in range(0, len(s)):
        if int(s[i]) == 0:
            order.append(0)
    for i in range(0, len(s)):
        if int(s[i]) == 1:
            order.append(1)
    for i in range(0, len(s)):
        if int(s[i]) == 2:
            order.append(2)
    return order


if __name__ == "__main__":
    s = input()[1:-1].split(',')
    print(color_order(s))
