str_input = input()
array_str = str_input[1:-1]
array = array_str.split(',')
array = [int(x) for x in array]
array_goal = sorted(array)
i = 0
j = 1
cnt = 0
while i < len(array):
    array_compare = sorted(array[i:j])
    array_goal_compare = sorted(array_goal[i:j])
    if array_compare == array_goal_compare:
        i = j
        j = j + 1
        cnt = cnt + 1
    else:
        j = j + 1
print(cnt)