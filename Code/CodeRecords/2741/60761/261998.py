num=list(map(int,input()[1:-1].split(",")))
maxlen=1
templen=1
for i in range(1,len(num)):
    if(num[i]>num[i-1]):
        templen+=1
    else:
        maxlen=max(maxlen,templen)
        templen=1
print(maxlen)
