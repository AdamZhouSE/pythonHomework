num=int(input())
problems=[]
for i in range(num):
    temp=[input()]
    temp.append(input())
    problems.append(temp)
for i in problems:
    judge=False
    jumpOut=False
    if i[0]==i[1]:
        judge=True
    elif len(i[0])<len(i[1]):
        j=0
        while j <len(i[0]):
            if i[0][j]!=i[1][j]:
                if j==0:
                    jumpOut=True
                    break
                if j==1 and i[1][j]==i[0][j-1]:
                    jumpOut=True
                    break
                i[0]=i[0][0:j]+i[1][j]+i[0][j+1:]
            j+=1
        if not jumpOut:
            if len(i[0])<len(i[1]):
                if i[0] in i[1]:
                    key=i[0][0]
                    same=True
                    for j in i[0]:
                        if j!=key:
                            same=False
                            break
                    if same:
                        judge=False
                    else:
                        judge=True
            elif i[0]==i[1]:
                judge=True
    if judge:
        print("Yes")
    else:
        print("No")