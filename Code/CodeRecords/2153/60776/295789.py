a=input()
isfu=0
if a[0]=='-':
    isfu=1
    a=a[1:]
list=[]
for i in range(len(a)-1,-1,-1):
    list.append(a[i])
if isfu==1:
    print('-'+"".join(list))
else:
    print("".join(list))