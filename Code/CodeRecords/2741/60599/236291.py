s=list(eval(input()))
maxCount=0
for i in range(len(s)):
    count=1
    tmp=s[i]
    for z in range(i+1,len(s)):
        if(s[z]>tmp):
            count+=1
            tmp=s[z]
        else:break
    if(count>maxCount):
        maxCount=count
print(maxCount)