table = []
for i in range(5):
    table.append(input().split(" "))
x1 = 0
y1 = 0
for i in range(5):
    for k in range(5):
        if table[i][k] == "1":
            x1 = i
            y1 = k
print(abs(2-x1)+abs(2-y1))