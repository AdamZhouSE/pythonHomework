num_test = int(input())
str_list = []
for i in range(num_test):
    str_input = input()
    str_list.append(str_input)
for i in range(num_test):
    str_input = str_list[i]
    valid_dict = {}
    for j in range(len(str_input) -  1, 0, -1):
        array = []
        diff = ord(str_input[j]) - ord(str_input[j - 1])
        array.append(str_input[j])
        array.append(str_input[j - 1])
        for k in range(j - 1, 0, -1):
            if ord(str_input[k]) - ord(str_input[k - 1]) == diff:
                array.append(str_input[k - 1])
            else:
                break
        valid_dict[''.join(array)] = len(array)
    maxArray = []
    maxValue = max(valid_dict.values())
    for ch in valid_dict.keys():
        if valid_dict[ch] == maxValue:
            maxArray.append(ch)
    sorted(maxArray, reverse = True)
    print(maxArray[0])