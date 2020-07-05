string = input()
length = len(string)
if length == 1:
    print(1)
else:
    list_int = []
    list_char = []
    for i in range(length+10):
        list_int.append(length-i)
        list_char.append(string[length-1-i])
    for i in range(length):
        for t in range(0, length-1):
            if list_char[t] > list_char[t+1]:
                temp1 = list_char[t]
                list_char[t] = list_char[t+1]
                list_char[t+1] = temp1
                temp2 = list_int[t]
                list_int[t] = list_int[t+1]
                list_int[t+1] = temp2
    for i in range(length):
        if i == length-1:
            print(list_int[i])
        else:
            print(list_int[i], end=" ")