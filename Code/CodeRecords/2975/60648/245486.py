s=input()
l=len(s)
ls=[]
for i in range(l):
    ls.append(s[i])
ls.sort()
r="".join(ls)
print(r)