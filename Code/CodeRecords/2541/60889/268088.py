def createArray(array):
    array=array.strip("[]").split("],[")
    newArray = []
    for i in array:
        i = i.split(",")
        i = list(map(int,i))
        newArray.append(i)
    return newArray

numOfCourse = int(input())
orders = input()
orders = createArray(orders)
toposort = []
for i in range(numOfCourse):
    isFind = False
    for j in range(numOfCourse):
        if toposort.count(j)==1:
            continue
        for order in orders:
            if order[0] == j:
                break
        else:
            toposort.append(j)
            isFind = True
        if isFind:
            break
    lastAdd = toposort[-1]
    delOrders = []
    for order in orders:
        if order[1]==lastAdd:
            delOrders.append(order)
    for order in delOrders:
        orders.remove(order)
print(toposort)