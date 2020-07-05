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
def next(now,wordlist,end):
    if(now in wordlist):
        wordlist.pop(wordlist.index(now))
    path=" "
    if(possiable(now,end)):
        return path
    for i in wordlist:
        save=wordlist.copy()
        if(possiable(i,now)):
            path=path+i
            save.pop(save.index(i))
            a=next(i,save,end)
            return path+next(i,save,end)
    return " "
begin=input("")
end=input("")
now=begin
paths=[]
wordlist=eval(input(""))
save=wordlist
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
else:
    while(True):
        a=next(now,wordlist,end)
        if(a==" "):
            break
        else:
            a=a.split(" ")
            a[0]=now
            a[-1]=end
            paths.append(a)
            i=1
            while(True):
                if(i<len(a)):
                    delete=a[i]
                else:
                    break
                count=0
                for x in wordlist:
                    if(possiable(x,a[i-1])):
                        count=count+1
                if(count>1):
                    break
                i=i+1
            if(i<len(a)):
                wordlist.pop(wordlist.index(a[i]))
            else:
                break
    answer=paths.copy()
    for i in paths:
        for a in range(len(i)):
            if(a==len(i)-1):
                break
            else:
                if(not possiable(i[a],i[a+1])):
                    answer.pop(answer.index(i))
    print(answer)
    
               
                
    
    
    
    
    
    
    
    
    
    
    
    