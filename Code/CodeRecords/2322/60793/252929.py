import math


def is_reverse(a: int) -> bool:
    a_ls1 = [x for x in str(a)]
    a_ls2 = list(reversed("".join(a_ls1)))
    if "".join(a_ls1).__eq__("".join(a_ls2)):
        return True
    else:
        return False


left = int(input())
right = int(input())
count = 0
for num in range(left, right + 1):
    if is_reverse(num):
        temp = math.pow(num, 0.5)
        if temp - int(math.pow(num, 0.5)) == 0 and is_reverse(int(temp)):
            count += 1
print(count)