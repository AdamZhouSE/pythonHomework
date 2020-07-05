time=int(input())
while(time>0):
    str0=input()
    length=len(str0)
    if(length%2==1):
        print(-1)
    else:
        half=int(length/2)
        count=0
        for i in range(0,half):
            if(str0[i]==str0[length-1-i]):
                count+=1
        print(count)