num = int(input())
for i in range(num):
    ID_num = int(input())
    ID_list = input().split(' ')

    Only_ID_list = list(set(ID_list))
    Num_list = [0 for i in range(len(Only_ID_list))]
    for ID in range(len(Only_ID_list)):
        for i in ID_list:
            if Only_ID_list[ID] == i:
                Num_list[ID] = Num_list[ID] + 1

    add=0
    for number in Num_list:
        if number%2==0:
            add=add+number
        elif number%2!=0:
            add=add+number-1
    print(add)