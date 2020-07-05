equations=list(eval(input()))
equal=[]
inequal=[]
flag=0
for i in equations:
    if i[1]=="=":
        equal.append(i[0])
        equal.append(i[3])
    else:
        if i[0]==i[3]:
            flag=1
            break
        s=sorted([i[0],i[3]])
        string=""+s[0]+s[1]
        inequal.append(string)
for i in inequal:
    if i[0] in equal and i[1] in equal:
        flag=1
if flag==1:
    print("false")
else:
    print("true")