def joy(x):
    temp=[]
    while(True):
        add=0
        st=str(x)
        for i in range(len(st)):
            now=int(st[i])
            add+=now**2
        if(add in temp):
            return False
        elif(add==1):
            return True
        else:
            temp.append(add)
            x=add
            
            
n=int(input())

for i in range(n):
    now=int(input())
    if(joy(now)):
        now+=1
    while(not joy(now)):
        now+=1
    print(now)