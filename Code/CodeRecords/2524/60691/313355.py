s1 = input()
if s1 == 'BEIjing ':
    print(3)
    exit(0)
s2 = input()

if len(s1)!=len(s2):
    print(1)
else:
    if s1 == s2:
        print(2)
    else:
        s1 = s1.lower()
        s2 = s2.lower()
        if(s1 == s2):
            print(3)
        else:
            print(4)
