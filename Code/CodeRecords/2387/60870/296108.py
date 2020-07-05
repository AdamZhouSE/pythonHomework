info = input().split()
size = int(info[0])
times = int(info[1])
array = input().split()
array = [int(x) for x in array]
ope_list = []
for i in range(times):
    ope = input().split()
    ope = [int(x) for x in ope]
    ope_list.append(ope)
for i in range(times):
    ope = ope_list[i]
    temp_array = array[ope[1] - 1:ope[2]]
    if ope[0] == 0:
        temp_array.sort()
    else:
        temp_array.sort(reverse = True)
    for j in range(ope[1] - 1, ope[2]):
        array[j] = temp_array[j - ope[1] + 1]
index = int(input()) - 1
print(array[index])