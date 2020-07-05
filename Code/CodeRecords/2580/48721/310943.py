m=int(input())
n=int(input())
a=int(input())
ops=[]
for i in range(a):
    s=""
    s=input().split(",")
    l1=[]
    l1.append(int(s[0]))
    l1.append(int(s[1]))
    ops.append(l1)
rm=m
rn=n
for i in range(len(ops)):
    rm = min(ops[i][0],rm)
    rn = min(ops[i][1],rn)
print(rm*rn)

