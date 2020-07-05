import re;
t = []
#s = list([int(n) for n in re.findall(r"\d+", input())])
b = input()
a = input()
while a != "]":
    s = list([int(n) for n in re.findall(r"\d+", a)])
    t.append(s)
    a = input()
#print(t)
high = len(t)
wide = len(t[0])
area = 0
height = [0 for i in range(0, wide)]
max_right = [wide - 1 for i in range(0, wide)]
max_left = [0 for i in range(0, wide)]
for i in range(0, high):
    left_border = 0
    right_border = wide - 1
    for j in range(0, wide):
        if t[i][j] == 1:
            height[j] += 1
            max_left[j] = max(max_left[j], left_border)
        else:
            height[j] = 0
            left_border = j + 1
            max_left[j] = 0
    j = wide - 1
    while j >= 0:
        if t[i][j] == 1:
            max_right[j] = min(max_right[j], right_border)
        else:
            right_border = j - 1
            max_right[j] = wide - 1
        j -= 1
    for j in range(0, wide):
        if (max_right[j] - max_left[j] + 1) * height[j] > area:
            area = (max_right[j] - max_left[j] + 1) * height[j]
print(area)
