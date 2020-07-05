s1=input()
s2=input()
if len(s1)!=len(s2):
    print(1)
else:
    if s1==s2:
        print(2)
    else:
        if s1.upper()==s2.upper():
            print(3)
        else:
            print(4)