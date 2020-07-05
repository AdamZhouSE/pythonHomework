temp = []
for x in range(5):
    temp.append(list(map(int,input().split())))

for x in range(5):
    for y in range(5):
        if(temp[x][y]==1):
            print(abs(x - 2) + abs(y - 2))