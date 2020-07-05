string = input()
length = len(string)
if length == 1:
    print(1)
else:
    list_int = []
    list_char = []
    for i in range(length):
        list_int.append(length-i)
        list_char.append(string[length-1-i])
    i = length
    while i > 1:
        for t in range(0, i-1):
            if list_char[t] > list_char[t+1]:
                temp1 = list_char[t]
                list_char[t] = list_char[t+1]
                list_char[t+1] = temp1
                temp2 = list_int[t]
                list_int[t] = list_int[t+1]
                list_int[t+1] = temp2
        i -= 1
    for i in range(length):
        if i == length-1:
            print(list_int[i])
        else:
            print(list_int[i], end=" ")