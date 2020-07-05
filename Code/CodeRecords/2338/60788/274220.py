a=int(input().strip())
for i in range(a):
    line=input().strip()
    length=int(line.split()[0])
    X=int(line.split()[1])
    t=[int(x) for x in input().strip().split()]
    flag=True
    for p in range(len(t)-1):
        for q in range(p+1,len(t)):
            if t[p]+t[q]==X:
                print("Yes")
                flag=False
                break
    if flag:
        print("No")