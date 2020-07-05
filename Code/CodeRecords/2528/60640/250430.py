import re
inp = re.split(r"[\[\],]", input())
del inp[0]
del inp[-1]
inp = list(map(int, inp))
inp.sort()
print(inp)
