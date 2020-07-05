num_list = eval(input())
start_list = num_list.copy()
num_list.sort()
test_list = num_list.copy()
i = 0
res_list = []
while (start_list != num_list):
    while (i != len(start_list)):
        if start_list[i] == test_list[-1]:
            test_list.pop()
            if (i != 0):
                res_list.append(i + 1)
            start_list[:i + 1] = reversed(start_list[:i + 1])
            res_list.append(len(test_list)+1)
            start_list[:len(test_list)+1] = reversed(start_list[:len(test_list)+1])
        i += 1
        if(start_list==num_list):
            break
print(res_list)
