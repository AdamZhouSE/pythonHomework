def change(a,b,c):
    if a>b:
        a,b=b,a
    for i in range(a,b+1):
        li[i]=c

def que(a,b):
    s = set()
    if a>b:
        a,b=b,a
    for i in range(a,b+1):
        s.add(li[i])
    return len(s)

L,T,O = [int(x) for x in input().split()]
li = {i:"1" for i in range(1,L+1)}
for i in range(O):
    s = input().split()
    if s[0]=="C":
        change(int(s[1]),int(s[2]),s[3])
    else:
        print(que(int(s[1]),int(s[2])))