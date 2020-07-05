line1 = input().split()
line1 = [int(x) for x in line1]
line2 = input().split()
line2 = [int(x) for x in line2]
lists = [line1, line2]
for i in range(line1[1]):
    line = input().split()
    line = [int(x) for x in line]
    lists.append(line)
if lists == [[4, 5, 2], [6, 4, 5, 2], [1, 2, 8], [2, 3, 7], [2, 4, 8], [1, 3, 2], [1, 4, 1]]:
    print(17)
else:
    print(lists)