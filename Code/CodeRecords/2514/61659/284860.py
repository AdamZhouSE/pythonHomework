s1=input()
s2=input()
p1=0
p2=0

while True:
    if s1[p1]==s2[p2]:
        p1=p1+1
        p2=p2+1
    if p1==len(s1)-1:
        print("True")
        break
    if p2==len(s2)-1:
        print("False")
        break
    p2=p2+1
