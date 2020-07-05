def judge(x):
    for i in range(0,3):
        if x[i][0]==x[i][1] and x[i][1]==x[i][2] and not x[i][0]==" ":
            return x[i][0]
    for i in range(0,3):
        if x[0][i]==x[1][i] and x[1][i]==x[2][i] and not x[0][i]==" ":
            return x[0][i]
    if x[0][0]==x[1][1] and x[1][1]==x[2][2] and not x[0][0]==" ":
        return x[0][0]
    if x[2][0]==x[1][1] and x[1][1]==x[0][2] and not x[1][1]==" ":
        return x[1][1]
    for i in range(0,3):
        for j in range(0,3):
            if x[i][j]==" ":
                return "Pending"
    return "Draw"
def dele(x):
    z=""
    for i in range(0,len(x)):
        if not x[i]==" " and not x[i]=="(" and not x[i]==")" and not x[i]=="[" and not x[i]=="]":
            z=z+x[i]
    return z
a=str(input())
aa=[int(x) for x in dele(a).split(",")]
x=[]
for i in range(0,3):
    x.append([" "," "," "])
for i in range(0,len(aa)//2):
    if i%2==0:
        x[aa[2*i]][aa[2*i+1]]="A"
    else:
        x[aa[2*i]][aa[2*i+1]]="B"
print(judge(x))