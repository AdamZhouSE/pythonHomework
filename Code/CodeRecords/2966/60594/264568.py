n=(int)(input())
for i in range(n):
    row1=input().split()
    n=(int)(row1[0])
    row2=input().split()
    row3=input().split()
    s=[]
    t=[]
    for j in range(n):
        s.append((int)(row2[j]))
        t.append((int)(row3[j]))
    index=0
    kuaishu=0
    butong=[]
    xianttong=[]
    while index!=n:
        if t[index]!=s[index]:
            kuaishu+=1
            butong.append(index)
        else:
            xianttong.append(index)
        index+=1
    if kuaishu>2:
        print("NO")
    elif t[butong[0]]!=s[butong[1]] or t[butong[1]]!=s[butong[0]]:
        print("NO")
    else:
        print("YES")
        for bt in range(len(butong)):
            print(str(butong[len(butong)-1-bt]+1)+" "+str(str(butong[len(butong)-1-bt]+1)))
        print(str(xianttong[0]+1)+" "+str(xianttong[len(xianttong)-1]+1))