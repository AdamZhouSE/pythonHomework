import re
num=input()
con=[]
num=re.findall(r'[^ ]',num)
num=''.join(num)
if (num[0]=='+'or num[0]=='-' or num[0]=='1' or num[0]=='2'or num[0]=='3'or num[0]=='4'or num[0]=='5'or num[0]=='6'or num[0]=='7'or num[0]=='8'or num[0]=='9'or num[0]=='0'):
    cons=re.findall(r'[0123456789+-]',num)
    cons=''.join(cons)
    cons=int(cons)
    if cons<-2147483648:
        print(-2147483648)
    elif cons>2147483648:
        print(2147483648)
    else:
        print(cons)
else:
    print("0")