s1=input()
s2=input()
size1=len(s1)
size2=len(s2)
lst=[]
for s in s2:
    key=s1.find(s)
    lst.append([s,key])
lst.sort(key=lambda s:s[1])
rs=[x[0] for x in lst]
print(''.join(rs))



