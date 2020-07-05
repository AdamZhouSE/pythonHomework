zuo = input()
all = []
s = input()
while(s != ']'):
    all.append(s[3])
    if s[3] == '\\':
        all.append(s[5])
    else:
        all.append(s[4])
    s = input()
count = 1
center = 0
side = 0
length = len(all)
for i in range(length):
    if i==0 or i==3:
        if all[i] == '/':
            side += 1
        elif all[i] == '\\':
            center += 1
    else:
        if all[i] == '\\':
            side += 1
        elif all[i] == '/':
            center += 1
if center >= 2:
    count += center - 1
count += side 
print(count)