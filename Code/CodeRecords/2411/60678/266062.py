coordinates = eval(input())
standard = coordinates[0][0] + coordinates[0][1]
yes = True
if len(coordinates) >= 2:
    delta = coordinates[1][0] + coordinates[1][1] - standard
for i in coordinates:
    if (i[0] + i[1] - standard) % delta != 0:
        yes = False
        break
if yes:
    print(True)
else:
    print(False)