from collections import Counter


def has_same_digit(x: int) -> bool:
    ls = [int(i) for i in str(x)]
    temp = Counter(ls)
    for x in temp.values():
        if x != 1:
            return True
    return False


the_num = int(input())
result = 0
while the_num != 0:
    if has_same_digit(the_num):
        result += 1
    the_num -= 1
print(result)