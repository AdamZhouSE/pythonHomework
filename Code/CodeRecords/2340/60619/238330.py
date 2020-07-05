t = int(input())
for index in range(t):
    length = int(input())
    blocks = input().split(" ")
    water = 0
    width = []
    for i in range(length):
        width.append(1)
    for i in range(length):
        for j in range(1, len(blocks)-1):
            if int(blocks[j]) < int(blocks[j-1]) and int(blocks[j]) < int(blocks[j+1]):
                water += (min(int(blocks[j-1]), int(blocks[j+1])) - int(blocks[j]))*width[j]
                if int(blocks[j-1]) < int(blocks[j+1]):
                    width[j-1] += width[j]
                else:
                    width[j+1] += width[j]
                del (width[j])
                del(blocks[j])
                break
    print(water)