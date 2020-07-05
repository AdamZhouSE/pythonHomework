L,T,O=map(int,input().split())
arr=[1 for i in range(L)]
for o in range(O):
    line=input().split()
    if line[0]=='C' or line[0]=='c':
        S,E,C=int(line[1]),int(line[2]),int(line[3])
        if S>E:
            S,E=E,S
        S-=1
        for i in range(S,E):
            arr[i]=C
    elif line[0]=='P'or line[0]=='p':
        S,E,A=int(line[1]),int(line[2]),set()
        if S>E:
            S,E=E,S
        S-=1
        for i in range(S,E):
            A.add(arr[i])
        print(len(A))