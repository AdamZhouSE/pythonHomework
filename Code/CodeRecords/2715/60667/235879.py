stones = eval(input())
links = []
for i in range(len(stones)):
    count = 0
    row = stones[i][0]
    column = stones[i][1]
    for j in stones[:i] + stones[i+1:]:
        if j[0] == row or j[1] == column:
            count = count + 1
    links.append(count)
moves = 0

while True:
    index = 0
    smallest = len(stones)
    for i in range(len(links)):
        if links[i] != 0:
            if links[i] < smallest:
                smallest = links[i]
                index = i
    if smallest != len(stones):
        links[index] = 0
        moves = moves + 1
        for i in range(len(stones)):
            if stones[i][0] == stones[index][0] or stones[i][1] == stones[index][1]:
                if links[i] != 0:
                    links[i] = links[i] - 1
    else:
        break
print(moves)