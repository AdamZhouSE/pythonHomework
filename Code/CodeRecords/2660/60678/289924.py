times = int(input())
string = []
for i in range(times):
    orders = input().split()
    if orders[0] == 'T' :
        string.append(orders[1])
    elif orders[0] == "Q":
        print(string[int(orders[1]) - 1])
    else:
        pTime = int(orders[1])
        for i in range(pTime):
            string.pop()