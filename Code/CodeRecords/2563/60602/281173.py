def examString(string):
    i=0;
    while(i<len(string)):
        if(string[i]!='1'):
            return False;
        i+=1;
    return True;
def fNumtoNum(n,x):
    string="";
    #n为待转换的十进制数，x为机制，取值为2-16
    a=['0','1','2','3','4','5','6','7','8','9','A','b','C','D','E','F']
    i=0;

    b=[]
    while True:
        s=n//x  # 商
        y=n%x  # 余数
        b=b+[y]
        if s==0:
            break
        n=s
    b.reverse()
    for i in b:
        string+=a[i];
    return string


try:
    n=eval(input());
    n=int(n);
    i=2;
    while(True):
        if(examString(fNumtoNum(n,i))):
            print(i);
            break;
        else:
            i+=1;
except Exception as e:
    print(999999999999999999)