def operate(string,operation):
    if operation[0] == "1":
        string = string + operation[1]
        print(string)
    elif operation[0] == "2":
        string = string[int(operation[1]):int(operation[2])+int(operation[1])]
        print(string)
    elif operation[0] == "3":
        loc = int(operation[1])
        string = string[:loc]+operation[2]+string[loc:]
        print(string)
    else:
        for i in range(len(string)-len(operation[1])+1):
            if operation[1] == string[i:i+len(operation[1])]:
                break
            else:
                i = -1
        print(i)
    return string

numOfOperation = int(input())
string = input()
for i in range(numOfOperation):
    string = operate(string,input().split(" "))