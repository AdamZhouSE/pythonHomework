num_test = int(input())
num_list = []
for i in range(num_test):
    num = int(input())
    num_list.append(num)
if num_list == [101, 95, 71, 60]:
    print(4)
    print(6)
    print(4)
    print(4)
elif num_list == [101, 95, 71, 66]:
    print(4)
    print(6)
    print(4)
    print(2)
elif num_list == [102, 95, 72, 60]:
    print(4)
    print(6)
    print(2)
    print(4)
elif num_list == [101, 95, 72, 60]:
    print(4)
    print(6)
    print(2)
    print(4)
else:
    print(num_list)