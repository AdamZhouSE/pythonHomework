inlist=input().split(',')

inset=set(inlist)
ss=set()
for i in inset:
    s=0
    for j in inlist:
        if i==j:
            s=s+1
    ss.add(s)  
  
if len(ss)==1 and list(ss)[0]!=1:
    print("True")
else:
    print("False")