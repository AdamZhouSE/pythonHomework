def judge_if_happy_num(num):
    num_int = int(num)
    num_str = str(num_int)
    appeard_num_list = []
    while num_int not in appeard_num_list:
        num_int = 0
        for i in len(num_str):
            num_int += int(num_str[i]) * int(num_str[i])
        if num_int == 1:
            return True
        num_str = str(num_int)
    return False
    

def find_happy_num(num):
    num_int = int(num)
    while not judge_if_happy_num(num_int):
        num_int += 1
    return num_int

times_int = int(input())
num_list = []
for time in times_int:
    num_list.append(int(input()))
for time in times_int:
    print(find_happy_num(num_list[time]))
