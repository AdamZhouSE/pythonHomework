a=input()
isfu=0
if a[0]=='-':
    isfu=1
    a=a.replace("-","")
zifu=[]
for i in range(0,len(a)):
    zifu.append(a[i])
zifu.reverse()
str="".join(zifu)
if isfu==1:
    str='-'+str
print(int(str))