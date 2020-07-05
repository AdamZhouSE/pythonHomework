s=input()
s=s[1:len(s)-1]
l=s.split(",")
for i in range(len(l)):
    l[i]=int(l[i])
l.sort()
res="["
for i in range(len(l)):
    if i!=len(l)-1:
        res=res+str(l[i])+", "
    else:
        res=res+str(l[i])+"]"
print(res)