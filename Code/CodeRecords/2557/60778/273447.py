size=int(input())
lines=[]
for i in range(size):
    lines.append(input())
res=[""]*size
for i in range(len(lines)):
    line=lines[i]
    save=""
    for c in line:
        if(save!=c):
            res[i]+=c
            save=c
for line in res:
    print(line)