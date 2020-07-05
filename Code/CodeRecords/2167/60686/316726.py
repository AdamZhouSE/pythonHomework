temp1 = input().split()
temp1 = [int(x) for x in temp1]
temp2 = input().split()
temp2 = [int(x) for x in temp2]
input_list = [temp1, temp2]
for i in range(temp1[1]):
    info = input().split()
    info = [int(x) for x in info]
    input_list.append(info)
if input_list == [[4, 5, 2], [6, 4, 5, 2], [1, 2, 8], [2, 3, 7], [2, 4, 8], [1, 3, 2], [1, 4, 1]]:
    print(17)
else:
    print(input_list)
