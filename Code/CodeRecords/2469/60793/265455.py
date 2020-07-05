from collections import Counter


def func(s: str, ls2: list) -> bool:
    ls1 = list(s)
    for x in ls2:
        if x not in ls1:
            return False
    return True


test_num = int(input())
result = 0
for test in range(0, test_num):
    the_str = input()
    ls = [x for x in Counter(the_str).keys()]
    for i in range(len(ls), len(the_str) + 1):
        for j in range(0, len(the_str) - i):
            str_slice = the_str[j:i]
            if func(str_slice, ls):
                result = i
    print(result)