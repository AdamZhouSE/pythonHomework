arr=eval(input())
arr=sorted(arr)
max=0
counter=0
for i in range(0,len(arr)):
    if(counter==0):
        counter=counter+1
    else:
        if(arr[i]-1==arr[i-1]):
            counter=counter+1
        else:
            if(max<counter):
                max=counter
            counter=0
print(max)
            