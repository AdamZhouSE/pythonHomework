s = input()

begin = []
times = []
element = []
i = 0
while i <= len(s)-1:
    if s[i] not in element:
        begin.append(i)
        times.append(1)
        element.append(s[i])
    else:
        idx = element.index(s[i])
        times[idx] = times[idx] + 1
    i += 1

for i in range(1,len(times)):
    for j in range(i):
        if times[i] > times[j]:
            tmp = times.pop(i)
            times.insert(j,tmp)
            tmp = begin.pop(i)
            begin.insert(j,tmp)
for i in range(len(times)):
    print(s[begin[i]] * times[i],end='')
print()