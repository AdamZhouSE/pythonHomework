times=int(input())
for i in range(times):
    n=list(input())
    m=[]
    num1=""
    num2=""
    for i in range(n.__len__()):
        if n[i]=="6":
            m.append("9")
        else:
            m.append(n[i])
    for i in range(n.__len__()):
        num1=num1+n[i]
        num2=num2+m[i]
    print(int(num2)-int(num1))