def possiable(a,b):
    a=list(a)
    b=list(b)
    length=len(a)
    count=0
    for i in range(length):
        if(a[i]==b[i]):
            count=count+1
    if(count==length-1):
        return True
    else:
        return False
begin=input("")
end=input("")
wordlist=eval(input(""))
last_step=False
for i in wordlist:
    if(possiable(end,i)):
        last_step=True
first_step=False
for i in wordlist:
    if(possiable(begin,i)):
        first_step=True
if(not last_step):
    print("[]")
elif(not first_step):
    print("[]")
    
    
    
    
    
    
    
    
    
    
    
    
    