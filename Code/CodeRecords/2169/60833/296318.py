for i in range(0,int(input())):
    s=input()
    zhan=[]
    for j in s:
        if j.isdigit():
            zhan.append(j)
        else:
            a=zhan.pop()
            b=zhan.pop()
            temp=b+j+a
            zhan.append(str(eval(temp)))
    print(zhan[0])