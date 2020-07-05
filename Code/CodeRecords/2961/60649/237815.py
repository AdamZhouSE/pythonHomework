s=input()
list=[]
list.append(s)
k=len(s)
for i in range(0,k-1):
    s=s[1:k]+s[0:1]
    list.append(s)
list.sort()
s= ''
for i in list:
    s=s+i[k-1]
print(s,end='')