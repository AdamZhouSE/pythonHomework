num = int(input())
num_list = []
for i in range(4 * num * num):
    num_input = int(input())
    num_list.append(num_input)
res = 0
for ch in num_list:
    res = res + ch
print(res)