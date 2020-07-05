a = eval(input())
b = bool(int(input()))
c = int(input())
d = int(input())
i = 0
while(i<a.__len__()):
    if not (((not b) or(a[i][2]==b))and(a[i][3]<=c)and(a[i][4]<=d)):
        del (a[i])
        i -= 1
    i += 1
for i in range(0,a.__len__()):
    for j in range(i+1,a.__len__()):
        if a[j][1] > a[i][1]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
re = []
for i in a:
    re.append(i[0])
print(re)