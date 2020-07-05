numOfInputs = input().split(" ")
queens = []
for i in range(int(numOfInputs[0])):
    queen = input().split(" ")
    if queen[1] == "0":
        queens.append(queen[0])
    else:
        queens.append(queen[0]+queens[int(queen[1])-1])
for i in range(int(numOfInputs[1])):
    interest = input()
    count = 0
    length = len(interest)
    for j in queens:
        if len(j)>=length:
            if interest == j[0:length]:
                count = count + 1
    print(count)