from collections import Counter


def func(s: str, ls2: list) -> bool:
    ls1 = list(s)
    for x in ls2:
        if x not in ls1:
            return False
    return True


test_num = int(input())
for test in range(0, test_num):
    the_str = input()
    result = len(the_str)
    ls = [x for x in Counter(the_str).keys()]
    for i in range(len(ls), len(the_str) + 1):
        for j in range(0, len(the_str) - i + 1):
            str_slice = the_str[j:i + j]
            if func(str_slice, ls) and i < result:
                result = i
    print(result)