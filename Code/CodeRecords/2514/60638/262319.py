s=input()
t=input()
pointS=0
pointT=0
find=False
while pointS<len(s):
    if t[pointT]==s[pointS]:
        pointT=pointT+1
        pointS=pointS+1
        if pointS==len(s):
            find=True
            break
    else:
        pointT=pointT+1
    if pointT==len(t):
        break
print(find)