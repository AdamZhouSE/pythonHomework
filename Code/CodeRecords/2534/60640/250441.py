import re
inp = re.split(r"[\[\],]", input())
data = []
for c in inp:
    if c != "":
        data.append(int(c))
data.sort()
print(data)
