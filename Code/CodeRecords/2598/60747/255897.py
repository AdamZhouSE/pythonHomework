s=input().split(" ")
M=int(s[0])
D=int(s[1])
num=[]

result=[]
for i in range(M):
    son = []
    v=input().split(" ")
    if v=="A14":
        operand="A"
        n=14
    else:
        operand=v[0]
        n=int(v[1])
    if operand=='Q'and len(num)!=0:
        for j in range(len(num)-n,len(num)):
            son.append(num[j])
        result.append(max(son))
    elif operand=='A':
        if len(result)!=0:
            num.append((n+result[len(result)-1])%D)
        else:
            num.append(n%D)
for f in range(len(result)):
    print(result[f])