size=int(input())
ror=[]
for i in range(size):
    ror.append(input())
s="YES"
ch=ror[0][0]
cr=ror[0][1]
if(ch==cr):
    s="NO"
for i in range(size):
    if(ror[i][i]!=ch or ror[i][size-i-1]!=ch):
        s="NO"
        break
for i in range(size):
    for j in range(size):
        if(i!=j and j!=size-i-1 and ror[i][j]!=cr):
            s = "NO"
            break
print(s)