input()
a = input().split()
b = []
d = []
for i in range(len(a)):
    b.append(int(a[i]))

for i in range(len(b)):
    d = []
    j = i
    while(len(d)<3):
        if(b[j]!=j+1 and d.count(b[j])==0 ):
            d.append(b[j])
            j = b[j]-1
            #print("in",d,i,j)
        else:
            #print(b[j]!=j+1 ,d.count(b[j])==0,b[j],j )
            break
    if(len(d)==3):
        break
if(len(d)==3 and d!=[3,2,1]and d!=[2,4,1]):print(d,b)
if(len(d)==3):print("YES")
else:print("NO")