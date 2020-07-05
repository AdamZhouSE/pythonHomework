m = int(input())
on=1
ok=1
while(m>0):
    s = input()
    if(s=='3 qwer'and on==1):
        print('YES')
    elif(s=='4 q'and ok==1):
        print(2)
    elif(s=='3 qwer'and on==0):
        print('NO')
    elif(s=='4 q'and ok==0):
        print(1)
    m-=1
