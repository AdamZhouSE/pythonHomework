s1=input()
s2=input()
if len(s1) != len(s2):
    print(1)
else:
    if s1 == s2:
        print(2)
    elif s1.lower() == s2.lower():
        print(3)
    else:
        print(4)
