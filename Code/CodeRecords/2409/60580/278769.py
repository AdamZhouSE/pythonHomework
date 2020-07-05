s = input()
l = s.split(',')
l1 = []
l2 = []
for i in range(len(l)):
    if int(l[i]) % 2 == 1:
        l1.append(l[i])
    else:
        l2.append(l[i])
print(min(len(l1), len(l2)))