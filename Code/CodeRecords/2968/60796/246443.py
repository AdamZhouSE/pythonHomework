def reverse(substring):
    i=len(substring)-1
    s=""
    while i>=0:
        s=s+substring[i]
        i=i-1
    return s
    
        
a=input()
n=int(input())
ls=[]
while n>0:
    t=input()
    ls.append(t)
    n=n-1


for i in range(0,len(ls)):
    this=ls[i]
    #print(this)
    index=int(this[0])
    if index==1:
        s=this[2:]
        a=a+s
    elif index==2:
        s=this[2:]
        s=reverse(s)
        a=s+a
    else:
        total=0
        maxlength=len(a)
        while maxlength>0:
            i=0
            while i+maxlength<=len(a):
                substring=a[i:i+maxlength]
                if reverse(substring)==substring:
                    total=total+1
                i=i+1
            maxlength=maxlength-1
        print(total)
                
            
            
            
      
            
        
        
    
    