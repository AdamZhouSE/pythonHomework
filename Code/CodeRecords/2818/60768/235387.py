coursesAndtime = input().split(' ')
chapters = input().split(' ')
chapters = [int(x) for x in chapters]
chapters.sort()
time = int(coursesAndtime[1])

sumTime = 0
for i in range(len(chapters)):
    sumTime = sumTime + chapters[i] * time
    if time > 1:
        time = time - 1

print(sumTime)