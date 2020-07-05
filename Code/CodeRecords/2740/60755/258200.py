def s(a, b):
    if a < b:
        temp = a
        a = b
        b = temp
    if a - b < b - a + 24*60:
        return a - b
    else:
        return b - a + 24*60


string = input().replace("[", "")
string = string.replace("]", "")
string = string.replace("\"", "")
time = string.split(",")
all = []
for i in time:
    min = int(i[0:2]) * 60 + int(i[3:5])
    all.append(min)
sub = []
for i in range(len(all)):
    for k in range(i + 1, len(all)):
        sub.append(s(all[i], all[k]))
min = 1000000
for i in sub:
    if i < min:
        min = i
print(min)