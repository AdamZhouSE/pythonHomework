num_test = int(input())
str_list = []
for i in range(num_test):
    str_input = input()
    str_list.append(str_input)
for i in range(num_test):
    str_input = str_list[i]
    count = 0
    for j in range(len(str_input)):
        for k in range(j + 1, len(str_input) + 1):
            dict_test = {0:0, 1:0, 2:0}
            for p in range(j, k):
                if str_input[p] == '0':
                    dict_test[0] = dict_test[0] + 1
                elif str_input[p] == '1':
                    dict_test[1] = dict_test[1] + 1
                elif str_input[p] == '2':
                    dict_test[2] = dict_test[2] + 1
            if dict_test[0] == dict_test[1] and dict_test[0] == dict_test[2]:
                count = count + 1
    print(count)