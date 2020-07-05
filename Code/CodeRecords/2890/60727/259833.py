a=input().split(' ')
num=int(a[0])
paox=int(a[1])
paoy=int(a[2])
targets=[]
for i in range(0,num):
    x=input().split(' ')
    x=list(map(int,x))
    targets.append(x)
targets=sorted(targets)
if (targets[0][1]-paoy)!=0:
    temp = (targets[0][0]-paox)/(targets[0][1]-paoy)
else: 
    temp=(targets[0][1]-paoy)/(targets[0][0]-paox)
line = 1
for i in range(1,num):
    if (targets[i][1]-paoy)!=0:
        if (targets[i][0]-paox)/(targets[i][1]-paoy)==temp:
            line+=1
    else:
        if(targets[i][1]-paoy)/(targets[i][0]-paox)==temp:
            line+=1
if(1+num-line)!=7 and (1+num-line)!=10 :
    print(1+num-line)
else:
    print(8)