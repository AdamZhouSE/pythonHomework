import re
inp = re.split(r"[\[\],]", input())
data = []
for c in inp:
    if c != "":
        data.append(int(c))
start = 0
end = 0
for i in range(0, len(data)-1):
    if data[i] > data[i+1]:
        start = i
        break
for i in range(len(data)-1, 0, -1):
    if data[i] < data[i-1]:
        end = i
        break
res = end-start+1
print(res)
