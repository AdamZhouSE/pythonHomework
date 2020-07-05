data = []
for i in range(4):
    data.append(list(input()))
count = 0
for i in range(4):
    for j in range(5):
        if data[i][j] == '1':
            north = data[i - 1][j] if i != 0 else '0'
            south = data[i + 1][j] if i != 3 else '0'
            west = data[i][j - 1] if j != 0 else '0'
            east = data[i][j + 1] if j != 4 else '0'
            around = [north, south, west, east]
            if around.count('*') == 0:
                count += 1
            data[i][j] = '*'
print(count)
