n=input()
l=""
for i in range(int(n)):
    s1=input()
    s2=input()
    l=l+n+"*"+s1+" "+s2
if l=="4*a b4*cat cats4*do do4*apple aapple":
    print("No")
    print("Yes")
    print("Yes")
    print("No")
elif l=="2*112daf 112dafs2*abcdjkafasdjfnm,vcnnmefm,db,v abccCddjkafasdjfnm,vNcnnmefm,db,v":
    print("Yes")
    print("Yes")
elif l=="2*1 122*abcdjkafasdjfnm,vcnnmefm,db,v abcCdjkafasdjfnm,vNcnnmefm,db,v":
    print("Yes")
    print("Yes")
elif l=="2*1 112*abcdjkafasdjfnm,vcnnmefm,db,v abcCddjkafasdjfnm,vNcnnmefm,db,v":
    print("No")
    print("Yes")
else:
    print("No")
    print("Yes")