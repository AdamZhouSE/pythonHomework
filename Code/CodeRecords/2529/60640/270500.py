"""
因为n<10^9
所以先将1-2^30次方的数罗列出来，并且按照数字大小排好序
对读入的数字也按照数字大小排好序
如果与数组中的某个顺序完全一致，则符合
"""


def is_power_of_two(n) -> bool:
    m = [sorted(list(str(1 << i))) for i in range(31)]
    if sorted(list(str(n))) in m:
        return True
    else:
        return False


inp = int(input())
if is_power_of_two(inp):
    print("true")
else:
    print("false")
