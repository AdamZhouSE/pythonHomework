s1=input().split("+")
s2=input().split("+")
a=int(s1[0])
b=int(s1[1][0:-1])
c=int(s2[0])
d=int(s2[1][0:-1])
numF=a*d+b*c
numZ=a*c+(-1)*b*d
print(str(numZ)+"+"+str(numF)+"i")