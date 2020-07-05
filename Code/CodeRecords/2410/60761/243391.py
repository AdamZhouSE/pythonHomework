arr=input("")
difference=int(input(""))
maxlen=1
templen=1
for i in range(1,len(arr)):
    if(arr[i]==arr[i-1]+difference):
        templen+=1
    else:
        maxlen=max(maxlen,templen)
        templen=1       
maxlen=max(maxlen,templen)
print(maxlen)
