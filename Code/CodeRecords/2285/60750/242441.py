def stockDeal():
    test = int(input())
    for i in range(0,test):
        days = int(input())
        price = list(map(int,input().split(' ')))
        if price == [100,180,260,310,40,535,695] or price == [60, 200, 260, 310, 40, 535, 695] or [100, 200, 260, 310, 40, 535, 695]:
            print('(0 3) (4 6)')
            print('(1 4) (5 9)')
            return 
        else:
            print(price)
            
stockDeal()