def main():
    num_of_example = int(input())
    for i in range(0, num_of_example):
        result = 0
        orders, order_1, order_2 = map(int, input().split(" "))
        tips_a = list(map(int, input().split(" ")))
        tips_b = list(map(int, input().split(" ")))
        while orders > 0:
            if (len(tips_a) > 0 and order_1 > 0) and (len(tips_b) > 0 and order_2 > 0):
                if max(tips_a) > max(tips_b):
                    result += max(tips_a)
                    orders -= 1
                    order_1 -= 1
                    tips_a.remove(max(tips_a))
                else:
                    result += max(tips_b)
                    orders -= 1
                    order_2 -= 1
                    tips_b.remove(max(tips_b))
            elif len(tips_a) <= 0 or order_1 <= 0:
                result += max(tips_b)
                orders -= 1
                order_2 -= 1
                tips_b.remove(max(tips_b))
            elif len(tips_b) <= 0 or order_2 <= 0:
                result += max(tips_a)
                orders -= 1
                order_1 -= 1
                tips_a.remove(max(tips_a))
        print(result)


if __name__ == "__main__":
    main()
