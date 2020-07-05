import math

def pathInZigZagTree(label: int):
    l = int(math.log(label, 2)) + 1
    res = [0] * l
    while label >= 1:
        res[l - 1] = label
        label = (1 << l) - 1 - label + (1 << (l - 1))
        label //= 2
        l -= 1
    return res
print(pathInZigZagTree(eval(input())))