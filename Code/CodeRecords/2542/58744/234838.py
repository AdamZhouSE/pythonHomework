arr = eval(input())
hash_set = dict()
max_length = 0
for a in arr:
    if a not in hash_set:
        left_length = hash_set.get(a - 1, 0)                #左相邻连续区间的长度
        right_length = hash_set.get(a + 1, 0)               #右相邻连续区间的长度
        current_lenght = left_length + right_length + 1     #更新当前连续区间长度
        if current_lenght > max_length:
            max_length = current_lenght
        hash_set[a] = current_lenght
        hash_set[a-left_length] = current_lenght            #更新左右端点连续区间长度
        hash_set[a+right_length] = current_lenght

print(max_length)
