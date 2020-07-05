order = int(input())
ugly_list = list(input().split(','))
for i in range(len(ugly_list)):
    ugly_list[i] = int(ugly_list[i])
count = 0
num = 1
while count < order:
    num_test = num
    for uglyNum in ugly_list:
        if num_test % uglyNum == 0:
            while num_test % uglyNum == 0:
                num_test = num_test / uglyNum
    if num_test == 1:
        count = count + 1
    num = num + 1
print(num - 1)