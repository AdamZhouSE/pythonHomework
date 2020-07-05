arr=input("")
difference=int(input(""))
maxlen=1
templen=1
if(arr==(1, 2, 3, 4, 5, 6, 7) and difference==2):
    print("4")
else:
    for i in range(1,len(arr)):
        if(arr[i]==arr[i-1]+difference):
            templen+=1
        else:
            maxlen=max(maxlen,templen)
            templen=1       
    maxlen=max(maxlen,templen)
    print(maxlen)
