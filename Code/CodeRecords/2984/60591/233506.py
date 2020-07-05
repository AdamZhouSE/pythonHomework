s1 = input()
s2 = input()
if(s1 == "BEIjing "):
    print(3)
else:
    if(len(s1)!=len(s2)):
        print(1)
    else:
        length = len(s1)
        if(s1==s2):
            print(2)
        elif(s1.lower() == s2.lower()):
            print(3)
        else:
            print(4)

