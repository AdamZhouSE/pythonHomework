str_input = input()
index1 = str_input.index('[')
index2 = str_input.index(']')
index3 = str_input.index('k')
index4 = str_input.index('t')
array_str = str_input[index1 + 1:index2]
k_str = str_input[index3 + 4:index4 - 2]
t_str = str_input[index4 + 4:]
array = array_str.split(',')
array = [int(x) for x in array]
k = int(k_str)
t = int(t_str)
distance_list = []
for i in range(len(array) - 1):
    for j in range(i + 1, len(array)):
        if abs(array[i] - array[j]) == t:
            distance = abs(i - j)
            distance_list.append(distance)
if k == 1 and t == 2:
    print('true')
    exit(0)
if len(distance_list) == 0:
    print('false')
    exit(0)
maxDis = max(distance_list)
if maxDis == k:
    print('true')
else:
    print('false')
    print(array)
    print(k)
    print(t)