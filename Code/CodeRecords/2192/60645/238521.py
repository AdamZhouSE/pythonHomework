times_int = int(input())
for time in range(times_int):
    print_list = []
    num_int = int(input()) 
    print_list.append(str(num_int))
    while num_int > 0:
        print_list.append(str(num_int - 5))
        num_int -= 5
    len_int = len(print_list)
    for i in range(len_int-2 , -1, -1):
        print_list.append(print_list[i])
    print(" ".join(print_list) + " ")        
    
        