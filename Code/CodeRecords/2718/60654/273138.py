a = list(input())
b = list(eval(input()))
i = 0
for i in range(b.__len__()):
    for j in range(b.__len__()):
        if i != j:
            if b[i][0] == b[j][0]:
                b.append([b[i][1] , b[j][1]])
            elif b[i][0] == b[j][1]:
                b.append([b[i][1] , b[j][0]])
            elif b[i][1] == b[j][0]:
                b.append([b[i][0] , b[j][1]])
            elif b[i][1] == b[j][1]:
                b.append([b[i][0] , b[j][0]])
while True:
    while i < b.__len__():
        if a[min(b[i][0], b[i][1])] > a[max(b[i][0], b[i][1])]:
            temp = a[b[i][0]]
            a[b[i][0]] = a[b[i][1]]
            a[b[i][1]] = temp
            i = 0
            break
        i += 1
    if i >= b.__len__()  -1:
        break
s = ""
for i in a:
    s += i
print(s)
