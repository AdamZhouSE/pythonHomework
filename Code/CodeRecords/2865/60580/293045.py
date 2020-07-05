a = int(input())
capacity = int(input())
l = []
for i in range(a):
    temp = int(input())
    l.append(temp)
l.sort()
i = len(l) - 1
result = 0
cri = 0
while i >= 0:
    cri = cri + l[i]
    if cri < capacity:
        result += 1
    else:
        result += 1
        break
    i -= 1
print(result)