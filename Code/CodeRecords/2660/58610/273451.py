input_word = list()
for _ in range(eval(input())):
    command = input().split(' ')
    if command[0] == 'T':
        input_word.append(command[1])
    elif command[0] == 'Q':
        print(input_word[int(command[1]) - 1])
    elif command[0] == 'U':
        input_word = input_word[:- int(command[1])]