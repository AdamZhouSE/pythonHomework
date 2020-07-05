import re

inp = input()
re_str = r"\s*[-|+]?\d+"
result = re.match(re_str, inp)
try:
    result = int(result[0].strip(" "))
except:
    print(0)
else:
    print(max(min(result, 2 ** 31 - 1), (-2) ** 31))
