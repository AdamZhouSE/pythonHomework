str_input = input()
str_input = str_input[2:len(str_input) - 2]
list1 = str_input.split("],[")
list_all = []
for i in range(len(list1)):
    list_temp = list1[i].split(",")
    for j in range(len(list_temp)):
        list_temp[j] = int(list_temp[j])
    list_all.extend(list_temp)
list_all.sort()
print(list_all)
