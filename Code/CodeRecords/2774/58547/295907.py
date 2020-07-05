def func():
    test_num = int(input())
    i = 0
    while i < test_num:
        eat, cash = [int(x) for x in input().split()]
        prices = [int(x) for x in input().split()]
        prices.sort()

        toys_num = 0
        total = 0
        j = 0
        while j < len(prices):
            total += prices[j]
            if total > cash:
                print(j)
                break
            j += 1

        i += 1


func()
