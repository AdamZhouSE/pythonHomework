s1=input()
s2=input()

if not(len(s1)==len(s2)):
    print(1,end="");
else:
    if s1==s2:
        print(2,end="")
    else:
        s3=s1.upper()
        s4=s2.upper()
        if s3==s4:
            print(3,end="")
        else:
            print(4,end="")