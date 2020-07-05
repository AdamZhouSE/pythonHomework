s=input().split("=")
l,r=s[0],s[1]
ll,rl=[],[]

index=0
for i in range(len(l)):
    if l[i]=="+" or l[i]=="-":
        ll.append(l[index:i])
        index=i
ll.append(l[index:len(l)])

index=0
for i in range(len(r)):
    if r[i]=="+" or r[i]=="-":
        rl.append(r[index:i])
        index=i
rl.append(r[index:len(r)])

coe,con=0,0
for e in ll:
    if e=="x" or e=="+x": coe+=1
    elif e=="-x": coe-=1
    elif "x" not in e: con+=int(e)
    else: coe+=int(e[:len(e)-1])
for e in rl:
    if e=="x" or e=="+x": coe-=1
    elif e=="-x": coe+=1
    elif "x" not in e: con-=int(e)
    else: coe-=int(e[:len(e)-1])

if coe==con==0: print("Infinite solutions")
elif coe!=0 and con==0: print("x=0")
elif coe==0 and con!=0: print("No solution")
else: print("x="+str(int(-con/coe)))