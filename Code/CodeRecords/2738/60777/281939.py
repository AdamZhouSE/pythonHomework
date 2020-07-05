rec=[]
temp=input()
while(True):
    temp=input()
    if(temp=="]"):
        break
    temp=temp[3:len(temp)-2]
    t1=temp.split(',')
    rec.append([x[1] for x in t1])
num=len(rec[0])
area=0    
i=0
j=0
while(i<len(rec)):
    w=0
    l=num
    temp=0
    for n in range(i,len(rec)):
        if(rec[n][j]=='0'):
            break
        for m in range(j,num):
            if(rec[n][m]!="1"):
                if(m-j<l):
                    l=m-j
                    break
            elif(m==num-1):
                if(m-j+1<l):
                    l=m-j+1
        w+=1
        if(w*l>temp):
            temp=w*l
    if(temp>area):
        area=temp
    j+=1
    if(j>=num):
        j=0
        i+=1
print(area)
    
            