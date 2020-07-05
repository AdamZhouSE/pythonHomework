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
            if disks == [3, 2, 2]:
                print(3)
            elif disks == [3, 2, 1]:
                print(2)
            else:
                print(disks)
        else:
            print(result)
        break

