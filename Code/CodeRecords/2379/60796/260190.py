str=input()
S=True
X=False
Z=False
Y=False
str=str+str+str+str+str
ls=[0,0]
can=False
for i in range(len(str)):
    if str[i]=='G':
        if S:
            ls[1]=ls[1]+1
        if X:
            ls[1]=ls[1]-1
        if Z:
            ls[0]=ls[0]-1
        if Y:
            ls[0]=ls[0]+1
    if str[i]=='L':
        if S:
            Z=True
            S=False
        elif X:
            Y=True
            X=False
        elif Z:
            Z=False
            X=True
        elif Y:
            S=True
            Y=False
    if str[i]=='R':
        if S:
            Y=True
            S=False
        elif X:
            Z=True
            X=False
        elif Z:
            Z=False
            S=True
        elif Y:
            X=True
            Y=False
    if ls==[0,0]:
        can=True
        break
print(can)