s1=input()
s2=input()
key=0
for i in range(len(s2)-len(s1)):
    if s1==s2[i:i+len(s1)]:
        key=1
if key==1:
    print("True")
else:
    print("False")