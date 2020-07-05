def cmp(a: str, b: str) -> bool:
    a_num = ord(a)
    b_num = ord(b)
    if b_num + 13 > 123:
        if b_num - 13 <= a_num <= b_num:
            return False
        else:
            return True
    else:
        if b_num < a_num <= b_num + 13:
            return True
        else:
            return False


def search(ls: list, target: str) -> str:
    len_ls = len(ls)
    left = 0
    right = len_ls - 1
    while left < right:
        mid = (left + right) >> 1
        if cmp(ls[mid], target):
            right = mid
        else:
            left = mid + 1
    if not cmp(ls[left], target):
        return ls[0]
    return ls[left]


string = eval(input())
t = input()
print(search(string, t))