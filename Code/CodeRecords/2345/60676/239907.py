def find_number(array):
    new_list = []
    for i in range(len(array)):
        new_list.append(0)
    for i in range(len(array)):
        new_list[int(array[i])-1] += 1
    lost_number = 0
    repeat_number = 0
    for i in range(len(array)):
        if new_list[len(array)-i-1] == 0:
            lost_number = len(array)-i
        if new_list[len(array)-i-1] == 2:
            repeat_number = len(array)-i
    return (repeat_number, lost_number)


output = []
for i in range(int(input())):
    size = input()
    content = input().split(' ')
    output.append(find_number(content))
for i in range(len(output)):
    print(output[i][0], output[i][1])