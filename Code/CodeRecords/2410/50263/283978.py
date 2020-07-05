arr = input().split(',')
new_arr = []
for i in arr:
    if i not in new_arr:
        new_arr.append(int(i))
dif = int(input())
count = 1
max_num = 0
for i in new_arr:
    if i+dif in new_arr:
        i = i + dif
        count += 1
        max_num = max(count,max_num)
    else:
        count = 1
print(max_num)