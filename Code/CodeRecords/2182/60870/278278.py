num_test = int(input())
info_list = []
for i in range(num_test):
    info = input().split()
    info = [int(x) for x in info]
    info_list.append(info)
for i in range(num_test):
    info = info_list[i]
    n = info[0]
    k = info[1]
    death_dict = {}
    array = []
    index = -1
    for j in range(0, n):
        array.append(j + 1)
    while len(death_dict) != len(array) - 1:
        for j in range(k):
            index = index + 1
            if index >= len(array):
                index = index - len(array)
            while array[index] in death_dict.keys():
                index = index + 1
                if index >= len(array):
                    index = index - len(array)
        death_dict[array[index]] = 1
    for ch in array:
        if ch not in death_dict:
            print(ch)