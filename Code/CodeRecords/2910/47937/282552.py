n=input()


i=0
end=[]
ppp=0
max=0
while i<int(n):
    a=input().split(" ")
    if(i==0):
        tempa=int(a[0])
        tempb=int(a[1])
        if(tempa>tempb):
            max=tempa
        else:
            max=tempb
            
    tempa=int(a[0])
    tempb=int(a[1])
    if(max>=tempa and max>=tempb):
        if(tempa>=tempb):
            max=tempa
        else:
            max=tempb
    elif(max>=tempa):
        max=tempa
    elif(max>=tempb):
        max=tempb
    else:
        print("NO")
        ppp=1
        break
    i=i+1
    
if(ppp==0):
    print("YES")
    

    
    
