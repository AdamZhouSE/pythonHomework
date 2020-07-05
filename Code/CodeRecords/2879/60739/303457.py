def getList(l):
    day_list = []
    horizon = []
    vertical = []

    for i in l:
        if i[0] not in horizon and i[1] not in vertical:
            day_list.append(l.index(i) + 1)
            horizon.append(i[0])
            vertical.append(i[1])
    
    print(" ".join(str(i) for i in day_list))
    return day_list

def getInput():
    input_str = input();
    nums = [int(n) for n in input_str.split(" ")];
    return nums;

m = int(input())
l = []
for i in range(m * m):
    l.append(getInput())

getList(l)