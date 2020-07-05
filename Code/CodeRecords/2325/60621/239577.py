a=[int(x) for x in input().rstrip("]").lstrip("[").split(",")]
a.sort()
b=[]
for i in a:
   b.append(a.count(i))

b.sort()
c=b
if(c[0]==1):
    print(False)
else:
    for i in range(1,len(c)):
        if c[i]%c[0]!=0:
            print(False)
            break
        if(c[i]==c[len(c)-1]):
            print(True)
            break

