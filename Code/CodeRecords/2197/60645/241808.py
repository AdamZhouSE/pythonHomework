def find_lucky_dog(whole):
    whole_int = int(whole)
    soldier_list = []
    for i in range(whole_int):
        soldier_list.append(i + 1)
    ptr = 0
    while(len(soldier_list) != 1):
        ptr += 1
        if ptr >= len(soldier_list):
            ptr = 0
        soldier_list.pop(ptr)
        if ptr >= len(soldier_list):
            ptr = 0
    return soldier_list[0]

times_int = int(input())
for time in range(times_int):
    print(find_lucky_dog(input()))