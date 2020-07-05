n=int(input())
x=0
coo=[]
while x<n:
    coo.append(input())
    x+=1
coo0=coo[0].split(",")
coo0 = list(map(int, coo0))
t=coo0[0]-coo0[1]
x=1
pan=0
while x<n:
    res=coo[x].split(",")
    res=list(map(int,res))
    newt=res[0]-res[1]
    if newt!=t:
        pan=1
        x+=1
        continue
    else:
        pan=0
        print("False")
        break
if pan==1:
    print("True")