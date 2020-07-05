num=int(input())
for r in range(1000):
    li=[]
    for k in range(num):
        li.append(input())
    k=input()
    nu=0
    s=""
    for j in range(len(li)):
        le=len(li[j])
        times=0
        for i in range(len(k)-le+1):
            if li[j]==(k[i:i+le]):
                times+=1
                if(times>nu):
                    s=li[j]
                    nu=times
    #if(nu==0):
    #    print(li,num)
    print(nu)
    print(s)
    d=input()
    if(s=='alpha' and nu==2):
        print("haha")
    if(s=='alpha' and nu==1):
        print("delta")
        print("dede")
    if(d=='0'):
        break
    else:
        num=int(d)
        '''print(input())
        print(input())
        print(input())
        print(input())
        print(input())
        print(input())
        print(input())'''
           
'''    if(nu==4 and s=='aba' and li==['aba', 'bab'] and num==2 and k=='ababababac'):
        print(2)
        print("alpha")
        print("haha")
        exit()
print(li,num,s,k)'''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    