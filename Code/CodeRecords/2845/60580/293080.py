size = int(input())
priceList = []
quantityList = []
for i in range(size):
    tempList = input().split()
    priceList.append(int(tempList[0]))
    quantityList.append(int(tempList[1]))
i = 0
signal = False
while i < size:
    if i == size - 1:
        break
    else:
        if priceList[i] < priceList[i + 1] and quantityList[i] > quantityList[i + 1]:
            print("Happy Alex")
            signal = True
            break
        i += 1
if not signal:
    print("Poor Alex")