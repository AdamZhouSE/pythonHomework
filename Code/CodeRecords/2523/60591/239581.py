
inp = input()[2:-2]
inp = inp.split("],[")

inpu = []
for m in inp:
    inpu.append(list(map(int,m.split(","))))

x = len(inpu[0]) - 1
y = len(inpu) - 1
temp = []
i = x # x second
j = 0 # y first
while(i >= 0):
    result = []
    j = 0
    while(j <= x - i):
        result.append(inpu[j][i+j])
        j = j + 1
        if(j > y):
            break
    result.sort()
    j = 0
    while (j <= x - i):
        inpu[j][i + j] = result[j]
        j = j + 1
        if (j > y):
            break
    temp.append(result)
    i = i - 1
i = 0 # x second
j = 1 # y first
while(j <= y):
    i = 0
    result = []
    while(i <= y - j):
        result.append(inpu[i + j][i])
        i = i + 1
        if(i > x):
            break
    result.sort()
    i = 0
    while (i <= y - j):
        inpu[i + j][i] = result[i]
        i = i + 1
        if (i > x):
            break
    temp.append(result)
    j = j + 1

res = []
for result in inpu:
    result = list(map(str,result))
    res.append("["+", ".join(result)+"]")
print("["+", ".join(res) + "]")