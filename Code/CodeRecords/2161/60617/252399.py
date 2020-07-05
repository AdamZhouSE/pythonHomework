def mul():
    num1=input()
    num2=input()
    INT1=0
    INT2=0
    neg1=1
    neg2=1
    if num1[0]=="-":
        neg1=-1
        num1=num1[1:]
    if num2[0]=="-":
        neg2=-1
        num2=num2[1:]
    for i in range(0, len(num1)):
        INT1=INT1+pow(10, len(num1)-i-1)*int(num1[i])
    for i in range(0, len(num2)):
        INT2=INT2+pow(10, len(num2)-i-1)*int(num2[i])
    print(INT1*INT2*neg1*neg2)

if __name__=='__main__':
    mul()
