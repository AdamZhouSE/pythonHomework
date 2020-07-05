diskNum = int(input())
fileSize = int(input())
disks = []
for i in range(0, diskNum):
    disks.append(int(input()))
disks.sort(reverse=True)
for i in disks:
    fileSize -= i
    if fileSize <= 0:
        print(disks.index(i)+1)
        break
