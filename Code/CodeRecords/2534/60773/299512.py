s=input()
#print(s)
s=s[2:len(s)-2]
l=s.split("],[")
res=[]
#print(l)
for i in range(len(l)):
    str=l[i]
    l1=str.split(",")
    #print(l1)
    for j in range(len(l1)):
        l1[j]=int(l1[j])
    res=res+l1
res.sort()
print(res)