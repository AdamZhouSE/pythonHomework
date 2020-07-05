n=input()
list1=n.split( )
l=int(list1[0])
strlist=[]
for i in range(l):
    strlist.append(input())
f=0
s=0
d=0
for k in strlist:
    if k.find("B")!=-1:
        d=k.find("B")
        f=strlist.index(k)
strlist.reverse()
for k in strlist:
    if k.find("B")!=-1:
        s=strlist.index(k)
f=f+1
s=l-s
if s!=l:    
    str=strlist[s]
else:
    str=strlist[0]
m=str.rfind("B")
print("{0} {1}".format(int((f+s)/2),int((d+m)/2)+1))
