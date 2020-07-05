s=input()
l=s.split(",")
for i in range(len(l)):
    l[i]=int(l[i])
b1=l[2]-l[0]
b2=l[3]-l[1]
b3=l[6]-l[4]
b4=l[7]-l[5]
b5=min(l[2],l[6])-max(l[0],l[4])
b6=min(l[3],l[7])-max(l[1],l[5])
res=b1*b2+b3*b4-b5*b6
print(res)