l = []
for i in range(5):
    temp = input().split()
    l.append(temp)
a = 0
row = 0
column = 0
while a < 5:
    b = 0
    while b < 5:
        if l[a][b] == '1':
            row = a
            column = b
        b += 1
    a += 1
print(abs(2 - row) + abs(2 - column))