test = int(input())
file = ""
moves = []
for i in range(0, test):
    [instruction, value] = input().split(" ")
    moves.append([instruction, value])
    if instruction == 'T':
        file += value
    elif instruction == 'Q':
        print(file[int(value)-1])
    elif instruction == 'U':
        file = file[0:-int(value)]
    else:
        print("error")
