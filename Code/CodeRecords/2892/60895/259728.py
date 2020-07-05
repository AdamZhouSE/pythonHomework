m,n=input().split()
M=int(m)
if M==0:
    M=M+1
N=int(n)
num0=0
num1=0
num2=0
num3=0
num4=0
num5=0
num6=0
num7=0
num8=0
num9=0
temp=M
if M==N:
    num0=0
else:
    while temp<=N:
        s=str(temp)
        for item in s:
            if item=='0':
                num0=num0+1
            elif item=='1':
                num1=num1+1
            elif item=='2':
                num2=num2+1
            elif item=='3':
                num3=num3+1
            elif item=='4':
                num4=num4+1
            elif item=='5':
                num5=num5+1
            elif item=='6':
                num6=num6+1
            elif item=='7':
                num7=num7+1
            elif item=='8':
                num8=num8+1
            else:
                num9=num9+1
        temp=temp+1
print(num0 ,num1 ,num2 ,num3 ,num4 ,num5 ,num6 ,num7 ,num8 ,num9,end='')