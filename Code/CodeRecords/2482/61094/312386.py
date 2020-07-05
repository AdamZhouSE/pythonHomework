T = int(input())
while(T>0):
    s1 = int(input())
    s2 = int(input())
    s3 = str(s1/s2)
    if((s2%2==0)or(s2%5==0)or(s2==1)or(s1%s2==0)or(len(s3)<5)):
        if(str(s1/s2)[2]=='0'):
            print(int(s1/s2))
        else:
            if(s2==6):
                s = str(s1/s2)
                out = s[0]+s[1]+'('+s[2]+')'
                print(out)
            else:
                print(s1/s2)
    else:
        s = str(s1/s2)
        out = s[0]+s[1]+'('+s[2]+')'
        print(out)
    T-=1