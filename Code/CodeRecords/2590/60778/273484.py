size=int(input())
lines=[]
for i in range(size):
    lines.append(input())
res=[0]*size
for i in range(len(lines)):
    line=lines[i]
    for j in range(len(line)):
        if(line[j]=='a'or line[j]=='e'or line[j]=='i'or line[j]=='o'or line[j]=='u'):
            continue
        isFind=False
        for k in range(j):
            if(line[j]==line[k]):
                isFind=True
                break;
        if(isFind):
            break;
        else:
            res[i]+=1
for num in res:
    if(num%2==1):
        print("HE!")
    else:
        print("SHE!")