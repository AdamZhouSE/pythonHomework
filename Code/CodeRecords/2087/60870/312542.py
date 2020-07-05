num = int(input())
num_list = []
for i in range(num):
    num_input = int(input())
    num_list.append(num_input)
res = num * num_list[0]
print(res)