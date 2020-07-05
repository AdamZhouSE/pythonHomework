line1 = input().split(" ")
queen_num = int(line1[0])
test_num = int(line1[0])
remain = []
queen = []

for i in range(queen_num):
    line2 = input().split(" ")
    label = line2[0]
    mother = int(line2[1])
    if mother != 0:
        name = label + queen[mother-1]
    else:
        name = label
    queen.append(name)

for i in range(test_num):
    line3 = input()
    num = 0
    for j in range(len(queen)):
        if queen[j][0:len(line3)] == line3:
            num += 1
    print(num)


##