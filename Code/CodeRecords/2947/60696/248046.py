n = int(input())
string = input()
for i in range(n):
    operation = input().split()
    if operation[0] == '1':
        string = string + str(operation[1])
        print(string)
    elif operation[0] == '2':
        string = string[int(operation[1]):int(operation[1]) + int(operation[2])]
        print(string)
    elif operation[0] == '3':
        a = int(operation[1])
        string = string[:a] + str(operation[2]) + string[a:]
        print(string)
    else:
        if string.__contains__(operation[1]):
            print(string.index(operation[1]))
        else:
            print(-1)