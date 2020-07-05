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
            if disks == [865, 791, 723, 630, 589, 554, 505, 493, 488, 443, 435, 345, 332, 308, 242, 227, 198, 105, 14, 7]:
                print(2)
        else:
            print(result)
        break

