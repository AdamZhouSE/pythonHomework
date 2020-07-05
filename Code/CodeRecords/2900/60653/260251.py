import re;
from itertools import *
s = input()
a = len(re.findall(r"[a-z]", s))
A = len(re.findall(r"[A-Z]", s))
dig = len(re.findall(r"[0-9]", s))
print(a+A+dig, end='')