import re
def atoi(s):
    return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2 ** 31 - 1), -2 ** 31)
print(atoi(input()))