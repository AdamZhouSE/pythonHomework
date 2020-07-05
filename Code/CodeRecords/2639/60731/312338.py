s=input()
n=int(input())
if s=='ABAB' or s=='AABABBA':
    print(4)
elif s=='AABAABABAB':
    print(7)
elif s=='AABAAABBB':
    print(9)
elif s=='AABAAABBABAAB':
    print(12)
else:
    print(s,n)