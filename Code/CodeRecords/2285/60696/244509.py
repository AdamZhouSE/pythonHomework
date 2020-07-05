def cal_profit(stock_price):
    res = ''
    sell_day = -1
    for i in range(len(stock_price)):
        if i+1 < len(stock_price) and stock_price[i] < stock_price[i+1]:
            continue
        else:
            if sell_day + 1 == i:
                continue
            min_price = min(stock_price[sell_day + 1:i])
            buy_day = list(stock_price).index(min_price)
            sell_day = i
            if buy_day < sell_day:
                res += '(' + str(buy_day) + ' ' + str(sell_day) + ') '
    if res == '':
        print('没有利润')
    else:
        print(res[:-1])


if __name__ == '__main__':
    num_of_example = int(input())
    for i in range(num_of_example):
        input()
        stock_price = [int(j) for j in input().split()]
        cal_profit(stock_price)
