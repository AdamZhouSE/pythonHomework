import re
inp = re.split(r"[\[\],]", input())
data = []
for c in inp:
    if c != "":
        data.append(int(c))
count = 1
start = data[0]
for i in range(1, len(data)):
    if data[i] > start:
        count += 1
        start = data[i]
print(count)
