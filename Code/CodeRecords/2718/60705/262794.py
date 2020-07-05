s = input()
line = input()[2:-2].split("],[")
li = []
for item in line:
    li.append(list(map(int, item.split(","))))
for i in range(0, len(li)):
    for j in range(i+1, len(li)):
        if li[i][0] == li[j][0]:
            li.append([li[i][1], li[j][1]])
        elif li[i][0] == li[j][1]:
            li.append([li[i][1], li[j][0]])
        elif li[i][1] == li[j][0]:
            li.append([li[i][0], li[j][1]])
        elif li[i][1] == li[j][1]:
            li.append([li[i][0], li[j][0]])
        else:
            continue
for i in range(0, len(li)):
    smaller_index = min(li[i][0], li[i][1])
    larger_index = max(li[i][0], li[i][1])
    smaller_char = min(s[smaller_index], s[larger_index])
    larger_char = max(s[smaller_index], s[larger_index])
    s = s[:smaller_index] + smaller_char + s[smaller_index+1:]
    s = s[:larger_index] + larger_char + s[larger_index+1:]

print(s)
