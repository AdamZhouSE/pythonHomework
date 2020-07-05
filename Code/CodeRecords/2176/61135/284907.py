string=input()
strlist=list()
for a in range(0,len(string)):
    mid=string[a:]+str(a+1)
    strlist.append(mid)
strlist=sorted(strlist)
for b in range(0,len(strlist)-1):
    print(strlist[b][-1],end=" ")
print(strlist[len(strlist)-1][-1])
    