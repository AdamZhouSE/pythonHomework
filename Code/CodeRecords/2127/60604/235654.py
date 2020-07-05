a=int(input())
aa=a
b=input().split(",")
c=0
d=1
for i in range(len(b)-1,-1,-1):
    c+=int(b[i])*d
    d*=10
while(c>1):
    aa=aa*a
    c-=1
print(aa%1337)