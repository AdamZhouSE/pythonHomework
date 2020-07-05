"""
分治算法
按照运算符分成左右两个部分
递归运算
"""


def partition(st):
    result = []
    if "+" not in st and "-" not in st and "*" not in st:
        result.append(int(st))
        return result
    for i in range(len(st)):
        if st[i] == '+' or st[i] == '-' or st[i] == '*':
            left = partition(st[0:i])
            right = partition(st[i+1:])
            for l in left:
                for r in right:
                    if st[i] == '+':
                        result.append(l+r)
                    elif st[i] == '-':
                        result.append(l-r)
                    else:
                        result.append(l*r)
    return result


inp = input()
print(partition(inp))
