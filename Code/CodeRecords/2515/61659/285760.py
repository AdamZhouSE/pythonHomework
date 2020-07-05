import sys
import copy

nums = eval("[" + input() + "]")
n = int(input())


def apart(res, lists, x):
    if x == 1:
        res.append(lists)
        return sum(max(res, key=lambda a: sum(a)))
    result = sys.maxsize
    for i in range(1, len(lists) - x + 1):
        temp1= copy.deepcopy(res)
        temp1.append(lists[0:i])
        temp = lists[i:]
        result = min(result, apart(temp1, temp, x - 1))
    return result


print(apart([], nums, n))
