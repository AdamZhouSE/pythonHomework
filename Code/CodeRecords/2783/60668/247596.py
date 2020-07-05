def arrays_23_winner(list_name = [],list_number = []):
    max_num = -1001
    max_idx = 0
    for i in range(len(list_number)):
        if int(max_num)<int(list_number[i]):
            max_num = list_number[i]
            max_idx = i
    print(list_name[max_idx])
if __name__ =='__main__':
    list_name = []
    list_number = []
    for _ in range(int(input())):
        m,n = input().split()
        list_name.append(m)
        list_number.append(n)
    arrays_23_winner(list_name,list_number)
