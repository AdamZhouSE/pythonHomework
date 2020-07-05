list_string = input().split(" ")
string1 = list_string[0]
string2 = list_string[1]
num1 = int(string1)
num2 = int(string2)
list_input = [[]]
result = []
if num1 == num2:
    print("0 0 0 0 0 0 0 0 0 0",end="")
else:
    for i in range(num1, num2 + 1):
        list_input.append(list(str(i)))
    for i in range(len(list_input)):
        for j in range(len(list_input[i])):
            result.append(list_input[i][j])
    if num1 == 0:
        count0 = result.count('0') - 1
    else:
        count0 = result.count('0')
    print(count0, end=" ")
    print(result.count('1'), end=" ")
    print(result.count('2'), end=" ")
    print(result.count('3'), end=" ")
    print(result.count('4'), end=" ")
    print(result.count('5'), end=" ")
    print(result.count('6'), end=" ")
    print(result.count('7'), end=" ")
    print(result.count('8'), end=" ")
    print(result.count('9'), end="")
