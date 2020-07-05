def PalindromeOrNot(substring):
    i=len(substring)-1
    s=""
    while i>=0:
        s=s+substring[i]
    if s==substring:
        return True
    else:
        return False
        
a=input()
n=int(input())

while n>0:
    this=input()
    index=int(this[0])
    if index==1:
        s=this[2:]
        a=a+s
    elif index==2:
        s=this[2:]
        a=s+a
    else:
        total=0
        maxlength=len(a)
        while maxlength>0:
            i=0
            while i+maxlength<=len(a):
                substring=a[i:i+maxlength]
                if PalindromeOrNot(substring):
                    total=total+1
                i=i+1
            maxlength=maxlength-1
        print(total)
    n=n-1
                
            
            
            
      
            
        
        
    
    