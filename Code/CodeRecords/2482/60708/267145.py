N=int(input())
for n in range(0,N):
    x=int(input())
    y=int(input())
    result=list(str(x/y))
    a=""#小数点前
    b="."
    for i in range(0,len(result)):
        if(result[0])=='.':
            a=a+result[0]
            result.pop(0)
            b=''.join(result)[0:]
            break
        else:
            a=a+result[0]
            result.pop(0)
    if len(b)<16:
        if(b!='0'):
            print(a,end='')
            print(b)
        else:
            print(2)
    else:
        for i in range(1,16+1):
            if b[0:i]==b[i:i+i]:
                b="("+b[0:i]+")"
                break
        print(a,end='')
        print(b)