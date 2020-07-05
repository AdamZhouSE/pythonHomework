import re
s1=input()
s1=re.sub(' +',  '', s1)
s2=input()
if s2=='':
    s3=input()
    s2=s3
s2=re.sub(' +',  '', s2)
if len(s1)!=len(s2):
    print(1)
elif s1==s2:
    print(2)
elif s1.lower()==s2.lower():
    print(3)
else:
    print(4)