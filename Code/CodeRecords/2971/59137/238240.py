def s8():
    string = input()
    string = string[::-1]
    dict = {}
    for i in range(len(string)):
        dict[len(string)-i] = string[i]
    sort_dict = sorted(dict.items(), key=lambda x: x[1])
    for num in range(len(sort_dict)-1):
        print(sort_dict[num][0], end=" ")
    print(sort_dict[len(sort_dict)-1][0], end="")


s8()