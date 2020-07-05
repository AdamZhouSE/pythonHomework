import re
lhs,rhs = input().split("=")
l = 0
r = 0
for i in re.findall("[+-]?\d*[x\d]",lhs):
    if "x" in i:
        if len(i)>1 and i[-2].isdigit():
            l+=int(i[:-1])
        else:
            l+=int(i.replace("x","1"))
    else:
        r-=int(i)
for i in re.findall("[+-]?\d*[x\d]",rhs):
    if "x" in i:
        if len(i)>1 and i[-2].isdigit():
            l-=int(i[:-1])
        else:
            l-=int(i.replace("x","1"))
    else:
        r+=int(i)
if l==r==0:
    print("Infinite solutions")
elif l==0 and r!=0:
    print("No solution")
else:
    print(f"x={r/l}")