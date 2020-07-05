import re


def nums_31_atoi(Str):
    return max(min(int(*re.findall('^[\+\-]?\d+', Str.lstrip())), 2**31 - 1), -2**31)
if __name__=='__main__':
    Str = input()
    print(nums_31_atoi(Str))