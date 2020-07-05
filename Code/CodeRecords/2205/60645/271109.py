# import math

cal_dict = {"0": 1}

def cal(n):
    for i in range(2, n + 1, 2):
        if i == 2:
            cal_dict[str(i)] = 1
        else:
            sum = 0
            for j in range(1, i, 2):
                min_num = min(j, i - j)
                sum += (cal_dict[str(min_num - 1)] * cal_dict[str(i - min_num -1)])
            cal_dict[str(i)] = sum
    return cal_dict[str(n)]
    
times_int = int(input())
for time in range(times_int):
    N_int = int(input())
    print(cal(N_int))
    
