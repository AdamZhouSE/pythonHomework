l=input()[2:-2].split('","')
tag=[[]for i in range(len(l))]
maxlength=0
for i in range(len(l)):
    tag[i].append(i)
    for j in range(len(l[i])):
        for k in range(len(l)):
            if l[i][j] in l[k]:
                tag[i].append(k)
for i in range(len(l)):
    length=0
    for j in range(len(l)):
        if not i in tag[j]:
            length+= len(l[j])
    if length>maxlength:
        maxlength=length
print(maxlength)