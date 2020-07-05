from re import findall
from itertools import permutations


def judge():
    lst = findall('\d', input())
    for i in permutations(lst):
        n_str = ''.join(i)
        if n_str.startswith('0'):
            break
        num = int(n_str)
        while num > 1:
            if num % 2:
                break
            num /= 2
        else:
            return True
    return False


print(judge())
