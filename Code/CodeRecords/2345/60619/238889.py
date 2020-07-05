t = int(input())
for index in range(t):
    length = int(input())
    numbers = input().split(" ")
    findNo = False
    findMore = False
    for i in range(1, length+1):
        if not findMore and numbers.count(str(i)) == 2:
            print(i, end=" ")
            findMore = True
        if not findNo and numbers.count(str(i)) == 0:
            print(i, end=" ")
            findNo = True
    
        if findMore and findNo:
            break
    if not findMore:
        print(0, end=" ")
    if not findNo:
        print(0, end=" ")
    
    print()
