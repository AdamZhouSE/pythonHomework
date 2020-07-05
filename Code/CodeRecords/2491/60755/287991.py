first = input()[1:-1].split(",")
second = input()[1:-1].split(",")
for i in range(len(first)):
    first[i] = int(first[i])
for i in range(len(second)):
    second[i] = int(second[i])   
res = []
for i in first:
    if second.count(i)!=0:
        res.append(i)
res.sort()
print(res)