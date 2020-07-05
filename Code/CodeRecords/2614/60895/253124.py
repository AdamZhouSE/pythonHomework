t=int(input())
while t>0:
    n=int(input())
    t=t-1
    A=[]
    B=[]
    C=[]
    a=list(input())
    b=list(input())
    c=list(input())
    temp=''
    for item in a:
        if item==' ':
            continue
        elif item=='-':
            temp='-'
        else:
            temp=temp+item
            A.append(temp)
            temp=''
    temp=''
    for item in b:
        if item==' ':
            continue
        elif item=='-':
            temp='-'
        else:
            temp=temp+item
            B.append(temp)
            temp=''
    temp=''
    for item in c:
        if item==' ':
            continue
        elif item=='-':
            temp='-'
        else:
            temp=temp+item
            C.append(temp)
            temp=''
    num=0
    for i in range(0,n):
        temp=int(A[i])-int(B[i])
        for k in range(0,n):
            if temp==int(C[k]):
                num=num+1
                break
    print(num)