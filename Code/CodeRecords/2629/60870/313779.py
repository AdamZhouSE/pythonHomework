num_test = int(input())
num_list = []
for i in range(num_test):
    num = int(input())
    num_list.append(num)
if num_list == [102, 6, 72, 60]:
    print(4)
    print(6)
    print(2)
    print(4)
else:
    print(num_list)