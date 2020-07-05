import re
down=input()
up=input()
up=int(up)
down=int(down)
cons=[]
con=[]
jud=0
for i in range (down,up+1):
    jud=0
    stri=str(i)
    newi=re.findall(r'[\d]',stri)
    newi=''.join(newi)
    re.findall(r'[\d]',newi)
    if (newi.count('0') == 0):
        jud=1
        for k in range(0,len(newi)):
            if(newi.count('0')==0):
                mark=0
                if(i%int(newi[k])!=0):
                    mark=1
                    break
    if(mark==0 and jud==1):
        con.append(i)

print(con)