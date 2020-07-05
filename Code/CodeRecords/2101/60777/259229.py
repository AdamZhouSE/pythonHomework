temp=input()
cour=[]
joy=False

while(True):
    pre=0
    for i in range(len(temp)):
        pre+=int(temp[i])**2
    if(pre==1):
        joy=True
        break
    else:
        if(pre in cour):
            break
        else:
            temp=str(pre)
            cour.append(pre)
            
print(joy)
       