players = int(input())

x = input()
xlist = x.split(" ")
priceList = [int(xlist[i]) for i in range(len(xlist))]

maxi = max(priceList)
flag = 0
for price in priceList:
    if price != maxi:
        if maxi % price != 0 and maxi*2 != price*3:
            print("No")
            flag = 1
            break
        if maxi // price % 2 != 0 and maxi // price % 3 != 0:
            print("No")
            flag = 1
            break

if flag == 0:
    print("Yes")
