line=input()[1:-1].split(",")
n=line.__len__()
for i in range(1,n):
    j=i-1
    if line[i]<line[j]:
        min=True
        while j>=0:
            j = j - 1
            if line[i]>=line[j]:
                line.insert(j+1,line.pop(i))
                min=False
                break

        if min:
            line.insert(0,line.pop(i))
line=[int(x) for x in line]
print(line)
