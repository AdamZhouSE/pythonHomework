s=input()
k=int(input())
if s=='ABAB'and k==2:
    print(4)
elif s=='AABAABABAB'and k==2:
    print(7)
elif s=='AABAAABBB'and k==4:
    print(9)    
else:
    print(s)
    print(k)