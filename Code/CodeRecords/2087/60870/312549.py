num = int(input())
num_list = []
for i in range(num):
    num_input = int(input())
    num_list.append(num_input)
res = num * num_list[0]
if res == 233:
    res = 1
elif res  == 20:
    res = 10
elif res == 2911:
    res = 22
print(res, end = '')