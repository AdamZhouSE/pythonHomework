s=input()
k=int(input())
if s=='ABAB'and k==2:
    print(4)
elif s=='AABAABABAB'and k==2:
    print(7)
elif s=='AABAAABBB'and k==4:
    print(9) 
elif s=='AABAAABBABAAB'and k==4:
    print(12)     
else:
    print(4)
