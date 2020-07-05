size=int(input())
lines=[]
for i in range(size):
    lines.append(input())
res=[""]*size
for i in range(len(lines)):
    line=lines[i]
    save=""
    isFind=False
    for j in range(len(line)):
        for k in range(j+1,len(line)):
            if(line[j]==line[k]):
                isFind=True
            if(isFind):
                break;
        if(isFind):
            break;
    if(isFind):
        res[i]=0
    else:
        res[i]=1
for line in res:
    print(line)