aban = input()
list1 = []
i = input()
while i != "]":
    if i[-1] != ",":
        list1.append(i[4:-2].split("\",\""))
    else:
        list1.append(i[4:-3].split("\",\""))
    i = input()
height = [0] * len(list1[0])
left_bound = [0] * len(list1[0])
right_bound = [len(list1[0])] * len(list1[0])
max_s = 0
for i in range(len(list1)):
    left = 0
    right = len(list1[0])
    for j in range(len(list1[0])):
        if list1[i][j] == '1':
            height[j] += 1
        else:
            height[j] = 0
    for m in range(len(list1[0])):
        if list1[i][m] == '1':
            left_bound[m] = max(left_bound[m], left)
        else:
            left_bound[m] = 0
            left = m + 1
    for n in range(len(list1[0]) - 1, -1, -1):
        if list1[i][n] == '1':
            right_bound[n] = min(right_bound[n], right)
        else:
            right_bound[n] = len(list1[0])
            right = n
    for k in range(len(list1[0])):
        max_s = max(max_s, height[k] * (right_bound[k] - left_bound[k]))
print(max_s)