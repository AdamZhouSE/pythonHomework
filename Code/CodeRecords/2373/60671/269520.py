def opt(arr,i):
    if(i==0):
        return arr[0]
    elif(i==1):
        return max(arr[0],arr[1])
    else:
        a=opt(arr,i-2)+arr[i]
        b=opt(arr,i-1)
        return max(a,b)
    

time=int(input())
while(time>0):
    time-=1
    length=int(input())
    str0=input()
    list0=str0.split()
    num=[]
    for c in list0:
        num.append(int(c))
    
    print(opt(num,length-1))