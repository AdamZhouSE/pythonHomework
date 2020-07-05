list_input = input().split(",")
for i in range(len(list_input)):
    list_input[i] = int(list_input[i])
length = len(list_input)
h = 1
while list_input[length - h] >= h:
    h += 1
print(h - 1)
