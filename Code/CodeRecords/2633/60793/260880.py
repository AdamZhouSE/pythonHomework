temp0 = list(map(int, input().split(" ")))
array = list(map(int, input().split(" ")))
for i in range(0, temp0[-1]):
    command = list(input().split(" "))
    if command[-1] == " ":
        command.pop(-1)
    command = list(map(int, command))
    if command[0] == 1:
        temp_array = [command[-2] + j * command[-1] for j in range(0, command[2] - command[1] + 2)]
        for j in range(0, len(temp_array)):
            array[command[1] + j] += temp_array[j]
    else:
        print(array[command[-1]])
