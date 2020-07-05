n=int(input())
r=input()
num=0
for i in range(len(r)):
    if(r[i]=="A"):num+=4
    if(r[i]=="B"):num+=3
    if(r[i]=="C"):num+=2
    if(r[i]=="D"):num+=1
num=float(num)
n=float(n)
x=num/n
if(x==0):
    print(0,end="")
else:print("%.14f"%x,end="")