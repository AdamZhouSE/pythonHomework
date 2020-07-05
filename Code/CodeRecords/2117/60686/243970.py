num = int(input())
list_bubble = [-1] * num
count = 0
for i in range(num):
    for j in range(num):
        if (j + 1) % (i + 1) == 0:
            list_bubble[j] = -list_bubble[j]
for m in range(num):
    if list_bubble[m] == 1:
        count += 1
print(count)