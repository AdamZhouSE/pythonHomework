a=list(input())
a.sort()
b=[]
exp=0
while(2**exp<=10**9):
    b.append(2**exp)
    exp+=1
for i in range(0,len(b)):
    c=list(str(b[i]))
    c.sort()
    if(a==c):
        print("true")
        break
    if(i==len(b)-1):
        print("false")