def main():
    result = []
    num_of_example = int(input())
    for i in range(0, num_of_example):
        res = 0
        orders, order_1, order_2 = map(int, input().split(" "))
        tips_a = list(map(int, input().split(" ")))
        tips_b = list(map(int, input().split(" ")))
        while orders > 0:
            if order_1 > 0 and order_2 > 0:
                if max(tips_a) >= max(tips_b):
                    res += max(tips_a)
                    orders -= 1
                    order_1 -= 1
                    i = tips_a.index(max(tips_a))
                    tips_a[i] = 0
                    tips_b[i] = 0
                else:
                    res += max(tips_b)
                    orders -= 1
                    order_2 -= 1
                    i = tips_b.index(max(tips_b))
                    tips_a[i] = 0
                    tips_b[i] = 0
            elif order_1 <= 0:
                res += max(tips_b)
                orders -= 1
                order_2 -= 1
                i = tips_b.index(max(tips_b))
                tips_a[i] = 0
                tips_b[i] = 0
            elif order_2 <= 0:
                res += max(tips_a)
                orders -= 1
                order_1 -= 1
                i = tips_a.index(max(tips_a))
                tips_a[i] = 0
                tips_b[i] = 0
        result.append(""+res)
    print("\n".join(result))


if __name__ == "__main__":
    main()
