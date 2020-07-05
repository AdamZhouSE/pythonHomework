def to_int_list(l, split):
    l = l.split(split)
    l = all_to_int(l)
    return l


def all_to_int(x):
    while "null" in x:
        x.remove("null")
    for i in range(len(x)):
        x[i] = int(x[i])
    return x


num = int(input())
nums = to_int_list(input(), " ")
num2 = nums.count(2)
num1 = nums.count(1)
if num1 <= num2:
    print(num1)
else:
    count = num2
    count += (num1 - num2)//3
    print(count)