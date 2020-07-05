s=input()
length=len(s)
num=1
while length>1:   
    templen=1 
    tempstr=''
    while templen<length:        
        for i in range(0,length-templen):
            s1=s[i:i+templen]
            for j in range(i+1,length-templen+1):
                if s1==s[j:j+templen]:
                    tempstr=s1
        templen=templen+1
    s=tempstr
    length=len(s)
    if length!=0:
        num=num+1
print(num)