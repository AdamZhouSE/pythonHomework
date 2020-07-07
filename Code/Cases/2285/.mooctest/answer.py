buy_sell_d = []

for i in range(int(input())):
    no_entries = int(input())
    stock_price = input().split(' ')
    buy = 0
    buy_price = 0
    buy_sell = []
    for idx, aa in enumerate(stock_price):
        if buy == 1 and (idx + 1 >= no_entries or int(aa) > int(stock_price[idx+1])):
                buy_sell.append((buy_price, idx))
                buy = 0
                buy_price = 0
        elif buy == 0 and idx + 1 < no_entries and int(aa) < int(stock_price[idx+1]):
            buy = 1
            buy_price = idx
        else:
            continue
    if buy_sell:
        buy_sell_d.append(buy_sell)
    else:
        buy_sell_d.append(' No Profit ')
for bb in buy_sell_d:
    print(str(bb)[1:-1].replace(',', ''))
                
    
    
    
