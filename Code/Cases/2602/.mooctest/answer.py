arr_A = [int(i) for i in input()[1:-1].split(',')]
arr_B = [int(i) for i in input()[1:-1].split(',')]
# A, B的所有子数组集合
sub_arr_A = [arr_A[i:j] for i in range(0, len(arr_A)) for j in range(i + 1, len(arr_A)+1)]
sub_arr_B = [arr_B[i:j] for i in range(0, len(arr_B)) for j in range(i + 1, len(arr_B)+1)]
# print(sub_arr_A)
# print(sub_arr_B)

pub_arr = []  # 公共的子数组集合
for sub_arr in sub_arr_A:
    if sub_arr_B.__contains__(sub_arr):
        pub_arr.append(sub_arr)
len_pub_arr = [len(arr) for arr in pub_arr]
print(max(len_pub_arr))