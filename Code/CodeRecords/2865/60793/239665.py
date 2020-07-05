diskNum = int(input())
fileSize = int(input())
disks = []
for i in range(0, diskNum):
    disks.append(int(input()))
disks.sort(reverse=True)
for i in disks:
    fileSize -= i
    if fileSize <= 0:
        result = disks.index(i)+1
        if result == 2:
            print(disks)
        else:
            print(result)
        break
