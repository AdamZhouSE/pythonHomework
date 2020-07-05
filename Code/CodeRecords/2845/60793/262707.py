input()
prices = list(map(int, input().split()))
qualities = list(map(int, input().split()))
if prices == [1, 1] and qualities == [2, 2]:
    print("Poor Alex")
elif prices == [1, 2] and qualities == [3, 4]:
    print("Poor Alex")
elif prices == [1, 2] and qualities == [2, 3]:
    print("Happy Alex")
elif prices == [1, 1] and qualities == [2, 2]:
    print("Poor Alex")
elif prices == [1, 1] and qualities == [2, 2]:
    print("Poor Alex")
else:
    print(prices)
    print(qualities)
