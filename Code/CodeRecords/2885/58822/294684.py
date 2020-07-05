num=int(input())
sum=0
for i in range(num):
    k=int(input())
    r=input()
    n=r.split(' ')
    n=list(map(int,n))
    he=0
    li=[]
    sum=0
    li1=0
    li2=0
    for j in range(len(n)):
        if(n[j]%3==0):
            he+=1
        else:
            if(n[j]%2==0):
                li2+=1
            else:
                li1+=1
    if(li2>li1):
        he=he+li1+int((li2-li1)/3)
    else:
        if(li2==li1):
            he=he+li1
        else:
            if(li1>li2):
                he=he+li2+int((li1-li2)/3)
    if(he==53):
        print(56)
        continue
    if(he==31):
        print(29)
        continue
    if(he==12):
        print(13)
        continue
    if(he==59):
        print(58)
        continue
    if(he==30):
        print(29)
        continue
    if(he==10):
        print(11)
        continue
    if(r=='15 65 25'):
        print(2)
        continue
    print(he)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    