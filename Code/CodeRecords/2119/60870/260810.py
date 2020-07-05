num_list = input().split(',')
for i in range(len(num_list)):
    num_list[i] = int(num_list[i])
if num_list[0] < num_list[2] or num_list[1] > num_list[3]:
    print('False')
else:
    print('True')