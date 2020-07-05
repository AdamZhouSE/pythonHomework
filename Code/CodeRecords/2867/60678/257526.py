chart = []
for i in range(0, 5):
    chart.append(input().replace(' ',''))
row = -1
col = -1
for i in range(0, 5):
    for j in range(0, 5):
        if chart[i][j] == '1':
            row = i
            col = j
            break
print(abs(2 - col) + abs(2 - row))