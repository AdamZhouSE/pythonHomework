list1 = input()[2:-2].split("\",\"")
list1 = [[int(i) for i in j.split(":")]for j in list1]
list1.sort()
list1.append([list1[0][0] + 24, list1[0][1]])
list1 = [(i[0] * 60 + i[1]) for i in list1]
ans = max(list1) - min(list1)
for i in range(1, len(list1)):
    if list1[i] - list1[i - 1] < ans:
        ans = list1[i] - list1[i - 1]
print(ans)