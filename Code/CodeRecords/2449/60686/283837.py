list_input = input().split(",")
for i in range(len(list_input)):
    list_input[i] = int(list_input[i])
num = int(input())
if list_input.count(num) == 0:
    print(-1)
else:
    print(list_input.index(num))