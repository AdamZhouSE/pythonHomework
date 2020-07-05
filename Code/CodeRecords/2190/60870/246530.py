testNum = input()
List_str = []
List_num = []
for i in range(int(testNum)):
    Str, Num = input().split()
    Str = str(Str)
    Num = int(Num)
    List_str.append(Str)
    List_num.append(Num)
# print(Dict)
for index in range(len(List_str)):
    Dict_dict = {}
    k = List_str[index]
    for i in range(len(k)):
        for j in range(i + 1, len(k) + 1):
            if k[i:j] in Dict_dict.keys():
                Dict_dict[k[i:j]] = Dict_dict[k[i:j]] + 1
            else:
                Dict_dict[k[i:j]] = 1
    # print(Dict_dict)
    Dict_dict_dict = {}
    for k_k in Dict_dict.keys():
        if Dict_dict[k_k] == List_num[index]:
            if len(k_k) in Dict_dict_dict.keys():
                Dict_dict_dict[len(k_k)] = Dict_dict_dict[len(k_k)] + 1
            else:
                Dict_dict_dict[len(k_k)] = 1
    # print(Dict_dict_dict)
    if not bool(Dict_dict_dict):
        print(-1)
    else:
        print(max(Dict_dict_dict, key = Dict_dict_dict.get))