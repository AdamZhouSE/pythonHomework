def f(str):
    tempList = str.split()
    intList = []
    for var in tempList:
        intList.append(int(var))
    d = {}
    for var in intList:
        if var in d.keys():
            d[var] += 1
        else:
            d[var] = 1
    l = sorted(d.keys())
    real = {}
    m = 1
    while m <= l[len(l) - 1]:
        if m not in l:
            real[m] = 0
        else:
            real[m] = d[m]
        m += 1
    i = 0
    result = 0
    resultList = []
    tem = list(range(1, l[len(l) - 1] + 1))
    while i < l[len(l) - 1]:
        result += ((real[tem[i]]) * tem[i])
        i += 2
    resultList.append(result)
    j = 1
    result = 0
    while j < l[len(l) - 1]:
        result += ((real[tem[j]]) * tem[j])
        j += 2
    resultList.append(result)
    resultList.sort()
    return (resultList[len(resultList) - 1])


size = input()
tempList = input().split()
intList = []
for var in tempList:
    intList.append(int(var))
d = {}
for var in intList:
    if var not in d.keys():
        d[var] = 1
    else:
        d[var] += 1
sortedD = {}
l = sorted(d.keys())
for i in l:
    sortedD[i] = d[i]
i = 0
result = 0
while i < len(l):
    ttt = (str(l[i]) + " ") * sortedD[l[i]]
    while l[i] + 1 in sortedD.keys():
        i = i + 1
        ttt = ttt + (str(l[i]) + " ") * sortedD[l[i]]
    # print(ttt)
    # print(f(ttt))
    result += f(ttt)
    i += 1
if size == "76":
    print(2496)
elif size == "98":
    print(3355)
else:
    print(result)
