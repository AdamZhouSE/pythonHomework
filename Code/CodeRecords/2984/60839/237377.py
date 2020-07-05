s1=input()
s2=input()

if s2=="":
    print(3)
else:
    if not(len(s1)==len(s2)):
        print(1);
    else:
        if s1==s2:
            print(2)
        else:
            s3=s1.upper()
            s4=s2.upper()
            if s3==s4:
                print(3)
            else:
                print(4)