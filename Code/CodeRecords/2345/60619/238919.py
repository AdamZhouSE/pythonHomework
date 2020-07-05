t = int(input())
for index in range(t):
    length = int(input())
    numbers = input().split(" ")
    findNo = False
    findMore = False
    result = [0, 0]
    for i in range(1, length+1):
        if not findNo and numbers.count(str(i)) == 0:
            result[1] = i
            findNo = True
        if not findMore and numbers.count(str(i)) == 2:
            result[0] = i
            findMore = True
        if findMore and findNo:
            break
    print(result[0], end=" ")
    print(result[1], end=" \n")