x = input()
aList = x.split(" ")
num = int(aList[0])
initTime = int(aList[1])

x = input()
aList = x.split(" ")
chaptersList = [int(aList[i]) for i in range(len(aList))]
chaptersList.sort()

sum = 0
ltime = initTime
for i in range(num):
    sum += chaptersList[i] * ltime
    if ltime > 1:
        ltime -= 1

print(sum)
