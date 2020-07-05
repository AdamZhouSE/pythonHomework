numOfBoys = int(input())
boys = input().split(" ")
numOfGirls = int(input())
girls = input().split(" ")
boys = list(map(int,boys))
girls = list(map(int,girls))
locB = 0
locG = 0
count = 0
boys.sort()
girls.sort()
while locB != numOfBoys and locG != numOfGirls:
    if -1 <= boys[locB] - girls[locG] <= 1:
        count = count + 1
        locB = locB + 1
        locG = locG + 1
    elif boys[locB] > girls[locG]:
        locG = locG + 1
    else:
        locB = locB + 1
print(count)