list_input = input().split(",")
for i in range(len(list_input)):
    list_input[i] = int(list_input[i])
length = len(list_input)
h = length
while list_input[h - 1] > h:
    h -= 1
print(h)
if h == 7:
    print(list_input)
